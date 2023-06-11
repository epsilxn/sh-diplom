# Generated by Django 4.2 on 2023-06-02 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_options_alter_companyservices_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='company',
            name='work_time',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Время работы'),
        ),
        migrations.AlterField(
            model_name='companyservices',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='company.company', verbose_name='Компания'),
        ),
    ]