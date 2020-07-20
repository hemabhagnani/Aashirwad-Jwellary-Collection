"""jwellary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path
from products import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contact"),
    path('collection/',include('products.urls')),
    path('singleproduct/<str:type>/<str:id>',views.singleproduct,name='singleproduct'),
    path('start99',views.start99,name='start99'),
    path('review',views.review,name='review'),
    path('sortby/<str:type>/<str:option>',views.sortby,name='sortby'),
    path('newcollection',views.newcollection,name='newcollection'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




