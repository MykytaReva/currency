from django.urls import path
from currency import views

app_name = 'currency'

urlpatterns = [
    path('rate/list/', views.RateListView.as_view(), name='rate_list'),
    path('rate/create/', views.RateCreateView.as_view(), name='rate_create'),
    path('rate/update/<int:pk>/', views.RateUpdateView.as_view(), name='rate_update'),
    path('rate/delete/<int:pk>/', views.RateDeleteView.as_view(), name='rate_delete'),
    path('rate/details/<int:pk>/', views.RateDetailView.as_view(), name='rate_details'),

    path('contact/us/', views.ContactUsListView.as_view(), name ='contactus_list'),
    path('contactus/create/', views.ContactUsCreateView.as_view(), name='contactus_create'),
    path('contactus/update/<int:pk>/', views.ContactUsUpdateView.as_view(), name='contactus_update'),
    path('contactus/delete/<int:pk>/', views.ContactUsDeleteView.as_view(), name='contactus_delete'),
    path('contactus/details/<int:pk>/', views.ContactUsDetailView.as_view(), name='contactus_details'),

    path('source/list/', views.SourceListView.as_view(), name='source_list'),
    path('source/create/', views.SourceCreateView.as_view(), name='source_create'),
    path('source/update/<int:pk>/', views.SourceUpdateView.as_view(), name='source_update'),
    path('source/delete/<int:pk>/', views.SourceDeleteView.as_view(), name='source_delete'),
    path('source/details/<int:pk>/', views.SourceDetailView.as_view(), name='source_details'),

]
