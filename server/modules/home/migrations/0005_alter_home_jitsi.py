# Generated by Django 4.2 on 2023-06-02 21:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_home_company_home_home_leader_alter_home_jitsi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='jitsi',
            field=models.CharField(blank=True, default=uuid.UUID('4f05549e-96d0-4d87-87e0-ce3be2762bed'), max_length=128, unique=True, verbose_name='GUID конференции'),
        ),
    ]