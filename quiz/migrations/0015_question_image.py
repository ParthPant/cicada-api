# Generated by Django 3.1.5 on 2021-01-16 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20210116_0421'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='question image'),
        ),
    ]