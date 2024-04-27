from django.urls import path
from .views import UsersProfileView, upload_avatar

urlpatterns = [
    path('profile', UsersProfileView.as_view(), name='user_profile'),
    path('profile/edit', UsersProfileView.as_view(), name='user_profile_edit'),
    path('upload_avatar', upload_avatar, name='upload_avatar'),
    path('profile/save', UsersProfileView.as_view(), name='save_user_profile'),
]
