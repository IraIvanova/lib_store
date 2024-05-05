from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag()
def get_user_avatar(request):
    if request.user.image:
        image_path = settings.MEDIA_URL + str(request.user.image)
    else:
        image_path = settings.STATIC_URL + 'img/avatardefault.png'

    return request.build_absolute_uri(image_path)
