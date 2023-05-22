from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, DetailView
from cars.core.mixins import AssignDataUpdateAdForm, generate_delete_code, \
    add_generated_delete_code_to_profile
from cars.profiles.forms import ProfileEditForm, ProfileCreateForm
from cars.profiles.models import Profile
from ..core.decorators import profile_required
from ..oauth_app.tasks import send_mail_async


# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileCreateView(UpdateView):
    model = Profile
    form_class = ProfileCreateForm
    success_url = reverse_lazy('index')
    template_name = 'profiles/create.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.is_activated = True
        return super().form_valid(form)
        # TODO: S


@method_decorator(profile_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileEditView(UpdateView, AssignDataUpdateAdForm):
    form_class = ProfileEditForm
    model = Profile
    template_name = 'profiles/edit-profile.html'

    def get_success_url(self):
        return reverse_lazy('edit profile')

    def get_object(self, queryset=None):
        return Profile.objects.filter(pk=self.request.user.pk).get()

    def form_valid(self, form):
        data = form.save(commit=False)
        profile = Profile.objects.get(pk=data.pk)
        self.asign_data_to_profile(profile, form)
        self.update_profile_image(profile, form)
        profile.save()
        return redirect(self.get_success_url())


@method_decorator(profile_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class ProfileDetailsView(DetailView, Paginator):
    model = Profile
    template_name = 'profiles/ads-profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.filter(user_id=self.request.user.pk).get()

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = {}

        profile = self.get_object()
        ad_set = profile.ad_set.all().order_by('-publication_date')

        paginator = Paginator(ad_set, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['object'] = profile
        context['page_obj'] = page_obj

        return context


@method_decorator(profile_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class DeleteCodeView(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        user = profile.user
        email = user.email
        delete_code = generate_delete_code()
        add_generated_delete_code_to_profile(delete_code, profile)
        send_mail_async.delay(email, delete_code)
        messages.success(request, "Check email for delete confirmation code.")
        return redirect('Delete user')
