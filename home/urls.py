from . import views
from django.urls import path

app_name='home'
urlpatterns = [
    path('', views.Home.as_view() , name='home'),
    path('questions/', views.QuestionListView.as_view()),
    path('questions/create/', views.CreateQuestionView.as_view()),
    path('questions/update/<int:pk>/', views.UpdateQuestionView.as_view()),
    path('questions/delete/<int:pk>/', views.DeleteQuestionView.as_view()),
]