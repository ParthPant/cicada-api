# Generated by Django 3.1.5 on 2021-01-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20210115_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is the quiz active'),
        ),
    ]
