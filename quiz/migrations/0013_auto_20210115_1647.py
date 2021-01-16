# Generated by Django 3.1.5 on 2021-01-15 16:47

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0012_quizinstance_curr_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='answer',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='quizinstance',
            unique_together={('quiz', 'taker')},
        ),
    ]
