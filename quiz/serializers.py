from rest_framework import serializers
from .models import Quiz, QuizInstance, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text', 'difficulty']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id' , 'name', 'description', 'date_published', 'num_questions']

class InstanceSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='taker.name', read_only=True)

    class Meta:
        model = QuizInstance
        fields = ['quiz', 'user_name', 'score']
