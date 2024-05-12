from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from custom_user.forms import CreateUserForm
from custom_user.models import CustomUser
from .tokens import account_activation_token


def register(request):
    if request.method == "POST":
        next = request.GET.get('next')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name="free_sub"))
            # user.save()
            login(request, user)
            if next:
                return redirect(next)
            else:
                return redirect('verify-email')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_vocabulary_list')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('chats')


def verify_email(request):
    if request.method == "POST":
        if request.user.email_is_verified != True:
            current_site = get_current_site(request)
            user = request.user
            email = request.user.email
            subject = "Verify Email"
            message = render_to_string('email/verify_email_message.html', {
                'request': request,
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
            return redirect('verify-email-done')
        else:
            return redirect('signup')
    return render(request, 'email/verify_email.html')


def verify_email_done(request):
    return render(request, 'email/verify_email_done.html')


def verify_email_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_is_verified = True
        user.save()
        messages.success(request, 'Your email has been verified.')
        return redirect('verify-email-complete')
    else:
        messages.warning(request, 'The link is invalid.')
    return render(request, 'email/verify_email_confirm.html')


def verify_email_complete(request):
    return render(request, 'email/verify_email_complete.html')
