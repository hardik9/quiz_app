from django.urls import path
from .views import new_quiz

urlpatterns = [
    path('quiz', new_quiz, name='quiz-page'),
]
