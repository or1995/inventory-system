from django.urls import path
from . import views


urlpatterns = [
    path('', views.items, name='home'),
    path('wshome', views.wsitems),
    path('add', views.form),
    path('additem', views.addItem),
    path('reader',views.codeReader),
    path('found',views.compare),
    path('check',views.codeCheck)
]