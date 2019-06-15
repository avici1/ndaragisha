"""ndaragisha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from api.views import *
from authentications.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/error/', error_view),
    path('', home_view),
    path('home/', home_view),
    path('dashboards/', dashboards),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/users/', user_view),
    path('api/handle_lost/', handle_lost_request),
    path('api/handle_found/', handle_found_items),
    path('api/get_lost/', get_all_items_lost),
    path('api/get_found/', get_all_items_found),
    path('api/get_all/',get_all_items),
    path('api/load/lost/', get_all_items_lost),
    path('api/contact_us/', handle_sent_messages),
    path('api/auth/signup/', signup_view),
    path('api/auth/process/signup/', custom_signup),
    path('api/auth/process/login/', custom_login)

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
