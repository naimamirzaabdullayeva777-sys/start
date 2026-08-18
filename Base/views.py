from django.shortcuts import render
from django.contrib.auth import login, logout

from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book, Shadow, Listening, Movie, User
from .serializers import (
    BookSerializer,
    ShadowSerializer,
    ListeningSerializer,
    MovieSerializer,
    RegisterSerializer,
)


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ShadowList(ListCreateAPIView):
    queryset = Shadow.objects.all()
    serializer_class = ShadowSerializer


class ListeningList(ListCreateAPIView):
    queryset = Listening.objects.all()
    serializer_class = ListeningSerializer


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# =========================
# REGISTER
# =========================

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            login(request, user)

            return Response(
                {
                    "success": True,
                    "message": "Ro'yxatdan o'tish muvaffaqiyatli!",
                    "username": user.username,
                    "phone": user.phone,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "success": False,
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


# =========================
# LOGIN
# =========================

class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {
                    "error": "Username va password kiriting."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {
                    "error": "Username yoki password noto'g'ri."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.check_password(password):
            return Response(
                {
                    "error": "Username yoki password noto'g'ri."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        login(request, user)

        return Response(
            {
                "success": True,
                "message": "Login muvaffaqiyatli!",
                "username": user.username,
                "phone": user.phone,
            },
            status=status.HTTP_200_OK,
        )


# =========================
# CURRENT USER
# =========================

class CurrentUserView(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            return Response(
                {
                    "is_authenticated": True,
                    "username": request.user.username,
                    "phone": request.user.phone,
                }
            )

        return Response(
            {
                "is_authenticated": False,
            }
        )


# =========================
# LOGOUT
# =========================

class LogoutView(APIView):

    def post(self, request):

        logout(request)

        return Response(
            {
                "success": True,
                "message": "Tizimdan chiqildi.",
            }
        )


def home(request):
    return render(request, "index.html")