from django.db import models
from django.utils import timezone
from datetime import datetime, date
from users.models import CustomUser

# Create your models here.

class Question(models.Model):
    DIFFICULTY = (
            (1, 'Easy'),
            (2, 'Moderate'),
            (3, 'Hard'),
        )

    question_text = models.TextField()
    image = models.ImageField(verbose_name='question image', blank=True, null=True)
    difficulty = models.IntegerField(default=1, choices=DIFFICULTY)
    correct_answer = models.CharField('correct answer', default='answer', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.question_text


class Quiz(models.Model):
    name = models.CharField(max_length=255, verbose_name='Quiz name')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Date of publication')
    date_active = models.DateField(verbose_name='Date of activation')
    description = models.TextField(blank=True)
    questions = models.ManyToManyField(Question, related_name='questions', blank=True)
    is_active = models.BooleanField('Is the quiz active', default=True)

    @property
    def num_questions(self):
        return self.questions.count()

    def __str__(self):
        return self.name

class QuizInstance(models.Model):
    taker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='taker')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_taken = models.DateTimeField(verbose_name='quiz taken', auto_now_add=True)
    score = models.IntegerField('score', default=0)
    complete = models.BooleanField(default=False)
    curr_question = models.IntegerField('Currently on question number', default=1)

    class Meta:
        unique_together = ('quiz', 'taker')

    @property
    def get_responses(self):
        return UserResponse.objects.filter(quiz_instance=self).all()

    @property
    def is_complete(self):
        return self.curr_question == self.quiz.num_questions

class UserResponse(models.Model):
    quiz_instance = models.ForeignKey(QuizInstance, on_delete=models.CASCADE)
    quesiton = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
