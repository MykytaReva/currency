from django.contrib import admin
from django.urls import path
from currency.views import generator


urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate/', generator)
]
