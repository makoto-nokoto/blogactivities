from django.urls import path
from . import views
urlpatterns = [
    path('activity/', views.activity_list, name='activity_list'),
    path('activity/<int:pk>/', views.post_detail, name='post_detail'),
    path('activity/new/', views.post_new, name='post_new'),
    path('activity/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('index/',views.index_page,name='index_page'),
    path('',views.index_page,name='home_page'),
    path('articles/',views.articles_page,name='articles_page'),
    path('links/',views.links_page,name='links_page'),
    path('todo/',views.todo_page,name='todo_page')
]
