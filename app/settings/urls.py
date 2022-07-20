from django.contrib import admin
from django.urls import path
from currency.views import rate_list, index, contact_us


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('contact/us/', contact_us),
    path('', index),
]
