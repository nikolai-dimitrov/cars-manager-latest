from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth import login
from cars.oauth_app.token import account_activation_token
from django.contrib import messages


def activate_account(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    else:
        messages.error(request, 'This activation link is invalid!')
    return redirect('Log in')


def send_email_activation_link(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('oauth_app/activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'

    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user} please go to your email {to_email} inbox and click on '
                                  f'received activation link to confirm and complete registration.')


def send_delete_code_to_email(to_email, delete_code):
    mail_subject = 'Profile delete confirmation code.'
    message = f'{delete_code}'
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        pass
