from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings


from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from currency.forms import RateForm, ContactUsForm, SourceForm
from currency.models import Rate, ContactUs, ResponseLog, Source


class IndexView(generic.TemplateView):
    template_name = 'currency/index.html'

    def get_context_data(self, *args, **kwargs):
        # breakpoint()
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        context['contactus_count'] = ContactUs.objects.count()
        context['source_count'] = Source.objects.count()
        return context


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'currency/my_profile.html'
    fields = (
        'first_name',
        'last_name',
    )
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class ResponseLogListView(LoginRequiredMixin, generic.ListView):
    queryset = ResponseLog.objects.all()
    template_name = 'currency/responselog_list.html'


class RateListView(LoginRequiredMixin, generic.ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'currency/rate_list.html'


class RateCreateView(generic.CreateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')


class RateUpdateView(UserPassesTestMixin, generic.UpdateView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_update.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, generic.DeleteView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_delete.html'
    success_url = reverse_lazy('currency:rate_list')

    def test_func(self):
        return self.request.user.is_superuser


class RateDetailView(generic.DetailView):
    queryset = Rate.objects.all()
    template_name = 'currency/rate_details.html'


class ContactUsListView(LoginRequiredMixin, generic.ListView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contactus.html'


class ContactUsCreateView(generic.CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contactus_create.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contactus_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        subject = self.object.subject
        message = self.object.message
        email_to = self.object.email_to

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email_to],
            fail_silently=False,
        )

        return response


class ContactUsUpdateView(LoginRequiredMixin, generic.UpdateView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contactus_update.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contactus_list')


class ContactUsDeleteView(generic.DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contactus_delete.html'
    success_url = reverse_lazy('currency:contactus_list')


class ContactUsDetailView(generic.DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contactus_details.html'


class SourceListView(LoginRequiredMixin, generic.ListView):
    queryset = Source.objects.all()
    template_name = 'currency/source_list.html'


class SourceCreateView(generic.CreateView):
    queryset = Source.objects.all()
    template_name = 'currency/source_create.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceUpdateView(generic.UpdateView):
    queryset = Source.objects.all()
    template_name = 'currency/source_update.html'
    form_class = SourceForm
    success_url = reverse_lazy('currency:source_list')


class SourceDeleteView(generic.DeleteView):
    queryset = Source.objects.all()
    template_name = 'currency/source_delete.html'
    success_url = reverse_lazy('currency:source_list')


class SourceDetailView(generic.DetailView):
    queryset = Source.objects.all()
    template_name = 'currency/source_details.html'
