from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import CustomUser

# Create your views here.
class CreateUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.filter(is_admin=False)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            token  = request.data['refresh_token']
            print(token)
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ListUsers(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = CustomUser.objects.filter(is_admin=False)
    serializer_class = UserSerializer
