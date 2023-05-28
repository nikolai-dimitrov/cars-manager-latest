from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, FormView, DetailView

from cars.core.decorators import unauthenticated_required, profile_required, staff_required
from cars.core.emails import send_email_activation_link
from cars.oauth_app.forms import UserRegisterForm, CustomAuthenticationForm, CustomChangePasswordForm

from cars.profiles.forms import ProfileDeleteCodeInputForm
from cars.profiles.models import Profile, DeleteCode

from django.contrib import messages


# Create your views here.


@method_decorator(unauthenticated_required, name='dispatch')
class UserRegisterView(CreateView):
    template_name = 'oauth_app/register.html'
    success_url = reverse_lazy('Log in')
    form_class = UserRegisterForm

    def form_valid(self, form):
        result = super().form_valid(form)
        send_email_activation_link(self.request, self.object, form.cleaned_data.get('email'))
        return result


@method_decorator(unauthenticated_required, name='dispatch')
class UserLogInView(LoginView):
    template_name = 'oauth_app/login.html'
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        if user.is_email_verified and not user.profile.is_banned:
            if user.profile.is_activated:
                return super().form_valid(form)
            else:
                login(self.request, user)
                return redirect('create profile')
        elif user.profile.is_banned:
            messages.error(self.request, f'Your profile is restricted!')
            return redirect('Log in')
        elif not user.is_email_verified:
            messages.error(self.request, f'Please verify your email')
            return redirect('Log in')


@method_decorator(profile_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class UserDeleteView(DetailView, FormView):
    USER_MODEL = get_user_model()
    model = Profile
    form_class = ProfileDeleteCodeInputForm
    template_name = 'profiles/delete-profile.html'
    success_url = reverse_lazy('Log in')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads = self.get_object().ad_set.order_by('-publication_date')[:4]
        context['ads'] = ads
        return context

    def get_object(self, queryset=None):
        return Profile.objects.filter(pk=self.request.user.pk).get()

    def form_valid(self, form):
        profile = self.get_object()
        profile_current_delete_code = DeleteCode.objects.get(profile=profile).generated_code
        confirmation_delete_code = form.cleaned_data['confirm_delete_code']

        if profile_current_delete_code != confirmation_delete_code:
            messages.error(self.request, f'Please enter valid confirmation code')
            return redirect('Delete user')

        user = self.USER_MODEL.objects.get(pk=self.get_object().pk)
        user.delete()
        return redirect(self.success_url)


@method_decorator(profile_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class UserChangePassword(PasswordChangeView):
    template_name = 'oauth_app/change-password.html'
    success_url = reverse_lazy('Log in')
    form_class = CustomChangePasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.request.user.pk)
        return context

    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)


@method_decorator(staff_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AdminControlView(ListView):
    model = Profile
    template_name = 'profiles/ban-page.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        sorted_context = super().get_context_data(object_list=None, **kwargs)
        sorted_context['paginator'].object_list.order_by('user_id')
        return sorted_context


@method_decorator(staff_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class BanUnbanView(View):
    model = Profile

    def get(self, request, *args, **kwargs):
        profile_pk = Profile.objects.get(pk=self.kwargs['pk'])
        profile = Profile.objects.get(pk=profile_pk)
        x = str(self.kwargs['page'])
        if self.request.user == profile.user or profile.user.is_staff or not self.request.user.is_staff:
            raise PermissionDenied()
        if profile.is_banned:
            profile.is_banned = False
        else:
            profile.is_banned = True
            user = profile.user
            user.is_active = False

        profile.save()
        return HttpResponseRedirect(f'/auth/user/admin/panel/?page={str(x)}')
