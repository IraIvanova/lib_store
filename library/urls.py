from django.urls import path
from .views import LibraryPage, LibraryDetailsPage

urlpatterns = [
    path('', LibraryPage.as_view(), name='library'),
    path('show/<int:id>', LibraryDetailsPage.as_view(), name='book_page'),
]
