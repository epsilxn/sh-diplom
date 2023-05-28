# Generated by Django 4.2 on 2023-05-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('start', models.DateTimeField(verbose_name='Начало')),
                ('end', models.DateTimeField(verbose_name='Конец')),
                ('timed', models.BooleanField(blank=True, verbose_name='Завершено')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Ивент',
                'verbose_name_plural': 'Ивенты',
            },
        ),
    ]
