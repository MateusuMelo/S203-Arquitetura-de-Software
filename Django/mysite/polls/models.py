import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Filme(models.Model):
    def __str__(self):
        return self.titulo
    titulo = models.CharField(max_length=25)
    ano_lancamento = models.DateTimeField("ano")
    diretor = models.CharField(max_length=25)
    genero = models.CharField(max_length=25)
    duracao = models.TimeField("duracao")
