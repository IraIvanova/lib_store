from external_api.dictionary import DictionaryAPI
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve, path, reverse
from services.files_handler import upload_file
from .forms import SearchWordForm, WordForm
from django.contrib.auth.models import Permission
from .models import UserVocabulary
from .utils import find_word_by_id
from datetime import date
import json

api = DictionaryAPI("http://127.0.0.1:8000/api/dictionary")


class UserVocabularyPage(UserPassesTestMixin, View):
    template_name = 'list.html'

    def test_func(self):
        return self.request.user.email_is_verified == True

    def get(self, request):
        user = request.user
        search_form = SearchWordForm()
        search_string = request.GET.get('search')

        words = list(UserVocabulary.objects.filter(user=user, language=user.learned_language))

        context = {
            'user': user,
            'search_form': search_form,
            'words': words
        }

        if search_string:
            search_results = api.search_translations(search_string, user.learned_language)

            context.update(
                {'words': [next((word for word in words if word.external_id == s['word_id']), s)
                           for s in search_results]})

        return render(request, self.template_name, context)


class UserVocabularyWordActionsView(View):

    def post(self, request):
        data = json.loads(request.body)
        word_id = data.get('word')
        user = request.user

        external_word = api.get_word_by_id(word_id, user.learned_language)[0]

        if not UserVocabulary.objects.filter(external_id=word_id, user=user, language=user.learned_language):
            today = date.today()

            if UserVocabulary.objects.filter(
                    created_at__date=today).count() >= 45 and user.groups.first().name != "premium_sub":
                return HttpResponse(json.dumps({'error': 'limit reached!'}), status=200)
            else:
                UserVocabulary.objects.update_or_create(user=request.user, external_id=word_id,
                                                        translation=external_word['translation'],
                                                        transcription=external_word['transcription'],
                                                        language=user.learned_language)
            context = {
                'message': 'Success!'
            }

            if data.get('page') == 'word':
                context.update(
                    {
                        'redirect': reverse('show_word_card', kwargs={'id': word_id})
                    }
                )
        else:
            return HttpResponse(json.dumps({'error': 'word already added!'}), status=200)

        return HttpResponse(json.dumps(context), status=200)

    def get(self, request, id=None):
        current_url = resolve(request.path_info).url_name
        word = find_word_by_id(id, request.user)
        additional_info = api.get_additional_info_for_word(id, request.user.learned_language)[0]

        if not word:
            word = additional_info
            return render(request, 'word_card_not_saved.html', {'word': word})

        form = WordForm(instance=word)
        transl_on_user_lang = list(
            filter(lambda x: (x['language'] == request.user.interface_language), additional_info['translations']))
        context = {
            'word': word,
            'word_form': form if current_url == 'edit_word_card' else None,
            'additional': {
                'synonyms': additional_info.get('synonyms'),
                'examples': additional_info.get('examples'),
                'translation_on_user_lang': transl_on_user_lang[0]['translation'] if transl_on_user_lang else ''
            }
        }

        return render(request, 'word_card.html', context)

    def delete(self, request, *args, **kwargs):
        print(request.body, 'jojojojo')
        data = json.loads(request.body)
        word_id = data.get('word')
        user = request.user
        print(data, 333)
        UserVocabulary.objects.filter(external_id=word_id, user=user, language=user.learned_language).delete()

        context = {
            'message': 'Word successfully deleted!'
        }

        if data.get('page') == 'word':
            context.update(
                {
                    'redirect': reverse('user_vocabulary_list')
                }
            )

        return HttpResponse(json.dumps(context), status=200)


class UserVocabularySaveWordView(View):
    def post(self, request):
        data = request.POST
        word_id = data.get('word_id')

        form = WordForm(data)
        word = find_word_by_id(word_id, request.user)

        if word and form.is_valid():
            word.examples = data.get('examples')
            word.save()

        return redirect("show_word_card", id=word_id)


def upload_word_image(request):
    data = request.POST
    user = request.user
    file = upload_file(request)
    word = UserVocabulary.objects.get(external_id=data.get('id'), user=user, language=user.learned_language)

    if file and word:
        word.image = file.file
        word.save()

        response = {
            'message': 'File was successfully uploaded',
            'path': settings.MEDIA_URL + str(file.file),
        }
        return HttpResponse(json.dumps(response), status=200)
    else:
        return HttpResponse(json.dumps({'message': 'File was not uploaded'}), status=400)
