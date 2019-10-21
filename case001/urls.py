from django.urls import path
from . import views
app_name = 'case001'

urlpatterns = [
    path('a8/', views.a8, name='a8'),
    # path('init_ww/', views.init_ww, name='init_ww'),
    # path('ww2/', views.ww2, name='ww2'),
    
    path('', views.index, name='index'),
]