"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ecommerce import settings
from ecommerce.views import home_page, about_page, contact_page, login_page, register_page


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', home_page, name='home'),
    url('^about/$', about_page, name='about'),
    url('^contact/$', contact_page, name='contact'),
    url('^login/$', login_page, name='login'),
    url('^register/$', register_page, name='register'),
    url('^products/', include('products.urls', namespace='products')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
