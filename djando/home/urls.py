from django.contrib import admin
from django.urls import path ,include
from home import views
urlpatterns = [
  path('',views.index, name='home'),
  path('HOME/',views.index, name='home'),
  path('CONTACT/', views.contact, name='contact'),
  path('BOYSFASHION/', views.boysfashion, name='boyssfashion'),
  path('GIRLSFASHION/', views.girlsfashion, name='girlsfashion'),
  path('TOYS/', views.toys, name='toys'),
  path('FOOTWEAR/', views.footwear, name='footwear'),
  path('FEEDING/', views.feeding, name='feeding'),
  path('HEALTH/', views.HEALTH, name='HEALTH'),
  path('ACCESSORY/', views.ACCESSORY, name='ACCESSORY'),
  path('DIAPERING/', views.DIAPERING, name='DIAPERING'),
  #path('boysfashion/', views.boysfashion, name='boyssfashion'),
  
]
