from django.db import models

# Create your models here.
class produto(models.Model):
    nome = models.CharField(max_lenght=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digit=10, decimal_place=2)
    estoque = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

