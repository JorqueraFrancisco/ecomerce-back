from django.shortcuts import render
from .models import User
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, LoginSerializer
from rest_framework.generics import CreateAPIView
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login, authenticate
from rest_framework.response import Response


class CreateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]


class UpdateUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            response = super(LoginView, self).post(request, format=None)
        else:
            response = Response({"error": "Invalid credentials"})

        return response
