from django.contrib import admin
from django.urls import path
from currency import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', views.rate_list),
    path('rate/create/', views.rate_create),
    path('rate/update/<int:rate_id>/', views.rate_update),
    path('rate/delete/<int:rate_id>/', views.rate_delete),
    path('rate/details/<int:rate_id>/', views.rate_details),

    path('contact/us/', views.contact_us),
    path('contactus/create/', views.contactus_create),
    path('contactus/update/<int:contactus_id>/', views.contactus_update),
    path('contactus/delete/<int:contactus_id>/', views.contactus_delete),
    path('contactus/details/<int:contactus_id>/', views.contactus_details),

    path('source/list/', views.source_list),
    path('source/create/', views.source_create),
    path('source/update/<int:source_id>/', views.source_update),
    path('source/delete/<int:source_id>/', views.source_delete),
    path('source/details/<int:source_id>/', views.source_details),

    path('', views.index),
]
