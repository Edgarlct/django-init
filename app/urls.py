from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
    path('post/', views.post, name='add_question'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    path('put/<int:question_id>/', views.put, name='put'),
]