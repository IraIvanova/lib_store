from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.urls import resolve
from custom_user.forms import EditUserForm
from services.files_handler import upload_file
import json


class UsersProfileView(View):
    template_name = 'user-profile.html'

    def get(self, request):
        user = request.user

        current_url = resolve(request.path_info).url_name
        form = EditUserForm(instance=user) if current_url == 'user_profile_edit' else None

        context = {
            'user': user,
            'user_image': settings.MEDIA_URL + user.image if user.image else settings.STATIC_URL + 'img/avatardefault.png',
            'user_form': form
        }

        return render(request, self.template_name, context)

    def post(self, request):
        if request.method == 'GET':
            return redirect('user_profile')

        user = request.user
        form = EditUserForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('user_profile')


def upload_avatar(request):
    file = upload_file(request)
    if file:
        user = request.user
        user.image = file.file
        user.save()

        response = {
            'message': 'File was successfully uploaded',
            'path': settings.MEDIA_URL + str(file.file),
        }
        return HttpResponse(json.dumps(response), status=200)
    else:
        return HttpResponse(json.dumps({'message': 'File was not uploaded'}), status=400)
