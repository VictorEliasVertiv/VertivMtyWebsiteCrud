# Generated by Django 4.0.8 on 2022-10-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_auto_20221010_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='Correo',
            field=models.EmailField(blank=True, default='default_email@email.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='CorreoSupervisor',
            field=models.EmailField(blank=True, default='default_email@email.com', max_length=254),
        ),
    ]