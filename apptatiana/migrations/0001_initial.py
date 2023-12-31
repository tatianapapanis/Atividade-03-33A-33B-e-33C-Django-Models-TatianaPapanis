# Generated by Django 3.2.13 on 2023-09-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_habilidade', models.CharField(max_length=50)),
                ('intensidade_habilidade', models.CharField(choices=[('P', 'Pouca'), ('M', 'Média'), ('G', 'Avançada')], max_length=1)),
                ('prioridade_habilidade', models.IntegerField()),
                ('classificacao_habilidade', models.CharField(choices=[('T', 'Técnica'), ('C', 'Comportamental'), ('A', 'Alta')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_hobbies', models.CharField(max_length=50)),
                ('descricao_hobbies', models.CharField(max_length=50)),
                ('intensidade_hobbies', models.CharField(choices=[('P', 'Pouca'), ('M', 'Média'), ('G', 'Avançada')], max_length=1)),
            ],
        ),
    ]
