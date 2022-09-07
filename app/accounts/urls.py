from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('my-profile/', views.UserProfileView.as_view(), name='my_profile'),
    path('activate/<uuid:username>/', views.UserActivateView.as_view(), name='user_activate'),
    ]
