from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, FormView

from cars.core.forms import CarSearchForm
from cars.core.mixins import CarApiMixin


# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(ListView, FormView, CarApiMixin):
    template_name = 'main/index.html'
    form_class = CarSearchForm
    object_list = []
    success_url = reverse_lazy('index')
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        self.get_cars(**form.cleaned_data)
        return super().form_valid(form)

    def get_cars(self, **data):
        x = data
        self.request.session['page'] = 1
        self.request.session['cars'] = self.make_request(**data)

    def get_queryset(self):
        # x = self.request.session.get('cars').clear()
        if self.request.session.get("page") is not None:
            return self.kwargs.get("cars") or self.request.session.get('cars') or []

        # if self.request.GET.get("page") is not None:
        #     return self.kwargs.get("cars") or self.request.session.get('cars') or []
        else:
            self.request.session["page"] = None
            self.request.session['cars'] = None
            return []


class AboutUsView(TemplateView):
    template_name = 'main/about-us.html'


def handle_not_found(request, exception):
    return render(request, 'main/not-found-404.html')


def handle_forbidden(request, exception):
    return render(request, 'main/forbidden-403.html')
