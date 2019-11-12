from django.db import models


class TrueFalseQuestion(models.Model):

    choice = [('True', 'True'), ('False', 'False')]

    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=5, choices=choice)

    def __str__(self):
        return self.question + ' -- ' + self.answer

