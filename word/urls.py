from django.urls import path
from word import views


app_name = 'word'
urlpatterns = [
    path('', views.WordListView.as_view(), name='list'),
    path('create/', views.WordCreateView.as_view(), name='create'),
    path('delete/list', views.WordDeleteListView.as_view(), name='delete_list'),
    path('delete/<int:pk>/', views.WordDeleteView.as_view(), name='delete'),
    ]
