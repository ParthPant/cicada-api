from django.urls import path
from django.shortcuts import redirect
from .views import ListQuiz, QuizView, LeaderboardView

app_name = 'quiz'

urlpatterns = [
    path('list/', ListQuiz.as_view(), name='list'),
    path('<int:quiz_id>/', QuizView.as_view(), name='quiz'),
    path('<int:quiz_id>/leaderboard', LeaderboardView.as_view(), name='leaderboard'),
]

