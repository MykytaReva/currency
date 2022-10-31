from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from accounts.forms import SignUpForm, CreateAvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserAvatar


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    queryset = get_user_model().objects.all()
    template_name = 'currency/my_profile.html'
    fields = (
        'first_name',
        'last_name',
        # 'avatar',

    )
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):

        return self.request.user


class UserAvatarView(generic.UpdateView):
    queryset = UserAvatar.objects.all()
    template_name = 'currency/avatar.html'
    fields = {
        'u_avatar'
    }
    success_url = reverse_lazy('index')


class UserAvatarCreateView(generic.CreateView):
    queryset = UserAvatar.objects.all()
    template_name = 'currency/avatar1.html'
    # fields = {
    #     'u_avatar'
    # }
    form_class = CreateAvatarForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    #
    # def save(self, commit=True):
    #     instance: UserAvatar = super().save(commit=False)
    #     instance.u_id = get_user_model().id
    #     instance.save()
    #     return instance


class SignUpView(generic.CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

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
