from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('my-profile/', views.UserProfileView.as_view(), name='my_profile'),
    path('my-profile/avatar/<int:pk>/', views.UserAvatarView.as_view(), name='avatar'),
    path('my-profile/avatar1/<int:pk>/', views.UserAvatarCreateView.as_view(), name='avatar1'),
    path('activate/<uuid:username>/', views.UserActivateView.as_view(), name='user_activate'),
    ]
