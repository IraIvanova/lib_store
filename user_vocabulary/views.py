from django.shortcuts import render
from django.views import View
from .forms import SearchWordForm
from .models import UserVocabulary
from external_api.dictionary import DictionaryAPI
from django.http import HttpResponse
import json

api = DictionaryAPI("http://127.0.0.1:8000/api/dictionary")


class UserVocabularyPage(View):
    template_name = 'list.html'

    def get(self, request):
        user = request.user
        search_form = SearchWordForm()
        search_string = request.GET.get('search')

        words = UserVocabulary.objects.filter(user=user).values_list('word', flat=True)

        context = {
            'user': user,
            'search_form': search_form,
            'words': words
        }

        if search_string:
            search_results = api.search_word(search_string)

            if words:
                context.update(
                    {'words': sorted([next((word for word in words if word['id'] == s['id'] and 'added' in word), s)
                                      for s in search_results], key=lambda s: s['word'])})

        return render(request, self.template_name, context)


class UserVocabularyWordActionsView(View):
    def post(self, request):
        data = json.loads(request.body)
        word_id = data.get('word')
        external_word = api.get_word_by_id(word_id)[0]

        if not UserVocabulary.objects.filter(external_id=word_id, user=request.user):
            external_word['added'] = True
            UserVocabulary.objects.get_or_create(user=request.user, external_id=word_id, word=external_word)
        else:
            return HttpResponse(json.dumps({'error': 'word already added!'}), status=200)

        return HttpResponse(json.dumps({'message': 'Success!'}), status=200)
