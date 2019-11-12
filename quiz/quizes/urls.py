from django.urls import path
from .views import new_quiz, quiz_home, add_q

urlpatterns = [
    path('', quiz_home, name='quiz-home'),
    path('quiz', new_quiz, name='quiz-page'),
    path('add', add_q, name='add-q'),
]
