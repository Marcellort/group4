from django.db import models
from django.contrib.auth.models import User

class Formularios(models.Model):
    Autor= models.ForeignKey(User, on_delete=models.CASCADE)
    Titulo= models.CharField(max_length=250)
    pergunta1= models.CharField(max_length=250)
    pergunta2= models.CharField(max_length=250)
    pergunta3= models.CharField(max_length=250)
    pergunta4= models.CharField(max_length=250)
    pergunta5= models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table="Formularios"

class Replies(models.Model):
    Responder = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=250)
    answer1 = models.CharField(max_length=250)
    answer2 = models.CharField(max_length=250)
    answer3 = models.CharField(max_length=250)
    answer4 = models.CharField(max_length=250)
    answer5 = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table="Replies"