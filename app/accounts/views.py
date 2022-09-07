from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'currency/my_profile.html'
    fields = (
        'first_name',
        'last_name',
        'avatar',

    )
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user


class SignUpView(generic.CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class UserActivateView(generic.RedirectView):

    pattern_name = 'index'

    def get(self, request, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(get_user_model(), username=username)

        if user.is_active:
            pass
        else:
            user.is_active = True
            user.save()

        response = super().get(request, *args, **kwargs)
        return response
