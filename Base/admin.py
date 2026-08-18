from django.contrib import admin
from .models import User, Book, Shadow, Listening, Movie, QuizQuestion


admin.site.register(User)

admin.site.register(Book)
admin.site.register(Shadow)
admin.site.register(Listening)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    list_filter = ("level",)
    search_fields = ("name",)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "question",
        "level",
        "topic",
        "correct_answer",
    )

    list_filter = (
        "level",
        "topic",
    )

    search_fields = (
        "question",
        "option_1",
        "option_2",
        "option_3",
        "option_4",
    )