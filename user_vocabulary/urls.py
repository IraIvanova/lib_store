from django.urls import path
from .views import UserVocabularyPage, UserVocabularyWordActionsView

urlpatterns = [
    path('list/', UserVocabularyPage.as_view(), name='user_vocabulary_list'),
    path('words/actions/', UserVocabularyWordActionsView.as_view()),
    # path('translations/', TranslationListCreateAPIView.as_view()),
]
