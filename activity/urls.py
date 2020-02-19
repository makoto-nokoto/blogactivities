from django.urls import path
from . import views
urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('activity/<int:pk>/', views.post_detail, name='post_detail'),
    path('activity/new/', views.post_new, name='post_new'),
    path('activity/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
