# Generated by Django 4.1.5 on 2023-02-12 17:05

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
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('times', models.BooleanField(blank=True)),
                ('description', models.TextField()),
            ],
        ),
    ]