from django.db import models

# Create your models here.


class Hobbies(models.Model):
    opcao = [
        ("P", "Pouca"),
        ("M", "Média"),
        ("G", "Avançada")
    ]

    tipo_hobbies = models.CharField(max_length=50)
    descricao_hobbies = models.CharField(max_length=50)
    intensidade_hobbies = models.CharField(max_length=1, choices=opcao)

class Habilidades(models.Model):
    options2 = [
        ("P", "Pouca"),
        ("M", "Média"),
        ("G", "Avançada")
    ]

    options3 = [
        ("T", "Técnica"),
        ("C", "Comportamental"),

    ]

    tipo_habilidade = models.CharField(max_length=50)
    intensidade_habilidade = models.CharField(max_length=1, choices=options2)
    prioridade_habilidade = models.IntegerField()  
    classificacao_habilidade = models.CharField(max_length=1, choices=options3)


class Idioma(models.Model):
  options4 = [
        ("B", "Básico"),
        ("M", "Intermediário"),
        ("F", "Fluente")
    ]

  nome = models.CharField(max_length=100)
  escola = models.CharField(max_length=100)
  classificacao = models.CharField(max_length=1, choices=options4)  