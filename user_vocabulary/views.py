from django.shortcuts import render
from django.views import View
from .forms import SearchWordForm
from external_api.dictionary import DictionaryAPI
import json

api = DictionaryAPI("http://127.0.0.1:8000/api/dictionary")


class UserVocabularyPage(View):
    template_name = 'list.html'

    def get(self, request):
        user = request.user
        search_form = SearchWordForm()
        search_string = request.GET.get('search')

        context = {
            'user': user,
            'search_form': search_form,
            'words': None
        }

        if search_string:
            words = api.search_word(search_string)
            print(words, 119)

            if words:
                context.update({'words': words})

        return render(request, self.template_name, context)


class UserVocabularyWordActionsView(View):
    def post(self, request):
        data = json.loads(request.body)
        word = data.get('word')


        print(data)
