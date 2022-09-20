from django.contrib import admin
from django.urls import path, include
from currency import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),

    path('accounts/', include('accounts.urls')),

    path('currency/', include('currency.urls')),

    path('api/v1/', include('api.v1.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('auth/', include('django.contrib.auth.urls')),
    ]

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
