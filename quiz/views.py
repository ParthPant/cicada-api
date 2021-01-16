from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import QuestionSerializer, QuizSerializer, InstanceSerializer
from .models import Question, Quiz, QuizInstance, UserResponse
from users.models import CustomUser

# Create your views here.

class LeaderboardView(ListAPIView):
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        return QuizInstance.objects.filter(quiz__pk = self.kwargs['quiz_id']).order_by('-score')

    serializer_class = InstanceSerializer

class ListQuiz(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.filter(is_active=True) 

class QuizView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, quiz_id, **kwargs):
        user = CustomUser.objects.get(pk=request.user.id)
        quiz = Quiz.objects.get(pk=quiz_id)
        query_set = QuizInstance.objects.filter(taker=user, quiz=quiz)
        num_instance = query_set.count()

        if num_instance > 0:
            instance = query_set.filter(taker=user, quiz=quiz)[0]
            num_q = instance.curr_question
        else:
            instance = QuizInstance(taker=user, quiz=quiz)
            instance.save()
            num_q = instance.curr_question

        if quiz.num_questions == 0:
            return Response('No Questions in the quiz')
        elif num_q > quiz.num_questions:
            return Response('Completed Quiz')

        question = quiz.questions.all()[num_q-1]

        serialiser = QuestionSerializer(question)
        return Response(serialiser.data)

    def post(self, request, quiz_id, **kwargs):
        '''
        get the answer, compare with the correct answer
        if answer is correct save score and increment current question number
        if answer is wrong and respond accordingly
        '''
        quiz = Quiz.objects.get(pk=quiz_id)
        user = CustomUser.objects.get(pk=request.user.id)
        instance = QuizInstance.objects.filter(taker=user, quiz=quiz)
        answer = request.data.get('answer')
        deltascore = 0

        if not instance:
            return Response('Invalid request')
        
        curr_question_num = instance[0].curr_question
        print(curr_question_num)
        curr_question = quiz.questions.all()[curr_question_num-1]

        if answer == curr_question.correct_answer:
            deltascore = curr_question.difficulty * 10

        instance[0].score += deltascore
        instance[0].curr_question += 1
        instance[0].save(update_fields=['score', 'curr_question'])

        user_resp = UserResponse(quiz_instance=instance[0], quesiton=curr_question, answer=answer)
        user_resp.save()
        
        return Response('Answer recorder')
