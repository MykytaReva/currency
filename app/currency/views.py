from django.urls import reverse_lazy
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from currency.filters import RateFilter
from currency.forms import RateForm, ContactUsForm, SourceForm
from currency.models import Rate, ContactUs, ResponseLog, Source
from django_filters.views import FilterView


from currency.tasks import send_email_contact_us


class IndexView(generic.TemplateView):
    template_name = 'currency/index.html'

    def get_context_data(self, *args, **kwargs):
        # breakpoint()
        context = super().get_context_data(**kwargs)
        context['rate_count'] = Rate.objects.count()
        context['contactus_count'] = ContactUs.objects.count()
        context['source_count'] = Source.objects.count()
        return context


class ResponseLogListView(LoginRequiredMixin, generic.ListView):
    queryset = ResponseLog.objects.all()
    template_name = 'currency/responselog_list.html'


# def api_get_rates_list(request):
#     queryset = Rate.objects.all().select_related('source')
#     response_content = []
#     for rate in queryset:
#         response_content.append({
#             'id': rate.id,
#             'buy': float(rate.buy),
#             'sale': float(rate.sale)
#         })
#     return JsonResponse(response_content, safe=False)


class RateListView(FilterView, generic.ListView):
    queryset = Rate.objects.all().select_related('source')
    template_name = 'currency/rate_list.html'
    paginate_by = 5
    filterset_class = RateFilter
    page_size_option = ['5', '10', '15', '20']

    def get_context_data(self, *args, **kwargs):
        context: dict = super().get_context_data(*args, **kwargs)
        filters_params = self.request.GET.copy()
        if self.page_kwarg in filters_params:
            del filters_params['page']

        context['filters_params'] = filters_params.urlencode()
        context['page_size'] = self.get_paginate_by()
        context['page_size_option'] = self.page_size_option
        return context

    def get_paginate_by(self, queryset=None):
        if 'page_size' in self.request.GET:
            paginate_by = self.request.GET['page_size']
        else:
            paginate_by = self.paginate_by
        return paginate_by


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
    paginate_by = 10


class ContactUsCreateView(generic.CreateView):
    queryset = ContactUs.objects.all()
    template_name = 'currency/contactus_create.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contactus_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_email_contact_us.delay(self.object.subject, self.object.message, self.object.email_to)

        return response

    def _send_email_contact_us(self):
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
