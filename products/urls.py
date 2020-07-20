from django.urls import path
from . import views


urlpatterns = [
    path('rings', views.rings,name='rings'),
    path('necklace',views.necklace,name='necklace'),
    path('bracelets', views.bracelets,name="bracelets"),
    path('earings', views.earings,name="earings"),
    path('jewellary', views.jewellary,name="jewellary"),
]


