from django.contrib import admin
from .models import Quiz, Question

class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    filter_horizontal = ('questions', )

# Register your models here.
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)

