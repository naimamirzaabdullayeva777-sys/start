from django.urls import path

from .views import (
    home,
    BookList,
    ShadowList,
    ListeningList,
    MovieList,
    RegisterView,
    LoginView,
    CurrentUserView,
    LogoutView,
)

urlpatterns = [
    path("", home, name="home"),

    path("api/books/", BookList.as_view(), name="books"),
    path("Shadow/", ShadowList.as_view(), name="Shadow"),
    path("Listening/", ListeningList.as_view(), name="Listening"),
    path("movie/", MovieList.as_view(), name="movie"),

    path("Register/", RegisterView.as_view(), name="Register"),
    path("login/", LoginView.as_view(), name="login"),
    path("CurrentUser/", CurrentUserView.as_view(), name="CurrentUser"),
    path("Logout/", LogoutView.as_view(), name="Logout"),
]