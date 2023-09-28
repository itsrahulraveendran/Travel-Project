from . import views
from django.urls import path

urlpatterns = [
      path('web', views.web, name='web'),
      path('',views.head,name='head'),
      path('website', views.website,name='website'),

]
