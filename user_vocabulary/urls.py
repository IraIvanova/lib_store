from django.urls import path
from .views import UserVocabularyPage, UserVocabularyWordActionsView, UserVocabularySaveWordView, upload_word_image

urlpatterns = [
    path('list/', UserVocabularyPage.as_view(), name='user_vocabulary_list'),
    path('words/', UserVocabularyWordActionsView.as_view(), name='add_word_to_list'),
    path('words/<int:id>', UserVocabularyWordActionsView.as_view(), name='show_word_card'),
    path('words/<int:id>/edit', UserVocabularyWordActionsView.as_view(), name='edit_word_card'),
    path('words/upload_word_image', upload_word_image, name='upload_word_image'),
    path('words/save', UserVocabularySaveWordView.as_view(), name='save_word'),
]
