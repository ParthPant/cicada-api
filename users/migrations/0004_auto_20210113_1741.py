# Generated by Django 3.1.5 on 2021-01-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='score',
            field=models.IntegerField(default=0, verbose_name='user score'),
        ),
    ]