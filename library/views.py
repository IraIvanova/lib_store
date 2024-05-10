from external_api.dictionary import DictionaryAPI
from django.views import View
from django.shortcuts import render
from .forms import SearchBookForm

api = DictionaryAPI("http://127.0.0.1:8000/api/library")


class LibraryPage(View):
    template_name = 'library.html'

    def get(self, request):
        user = request.user
        search_form = SearchBookForm()
        search_string = request.GET.get('search')

        context = {
            'user': user,
            'search_form': search_form,
            'books': api.get_book_list(search_string if search_string else '', user.learned_language)
        }

        return render(request, self.template_name, context)


class LibraryDetailsPage(View):
    # def post(self, request):
    #     data = json.loads(request.body)
    #     word_id = data.get('word')
    #     user = request.user
    #
    #     external_word = api.get_word_by_id(word_id, user.learned_language)[0]
    #
    #     if not UserVocabulary.objects.filter(external_id=word_id, user=user, language=user.learned_language):
    #         UserVocabulary.objects.update_or_create(user=request.user, external_id=word_id,
    #                                                  translation=external_word['translation'],
    #                                                  language=user.learned_language)
    #         context = {
    #             'message': 'Success!'
    #         }
    #         print(data)
    #
    #         if data.get('page') == 'word':
    #             context.update(
    #                 {
    #                     'redirect': reverse('show_word_card', kwargs={'id': word_id})
    #                 }
    #             )
    #     else:
    #         return HttpResponse(json.dumps({'error': 'word already added!'}), status=200)
    #
    #     return HttpResponse(json.dumps(context), status=200)

    def get(self, request, id=None):
        book = api.get_book_by_id(id)
        context = {
            'book': book,
        }

        return render(request, 'book_page.html', context)
