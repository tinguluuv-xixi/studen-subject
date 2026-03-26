from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('them/', views.them_sinh_vien, name='them'),
    path('sua/<int:pk>/', views.sua_sinh_vien, name='sua'),
    path('xoa/<int:pk>/', views.xoa_sinh_vien, name='xoa'),
]
