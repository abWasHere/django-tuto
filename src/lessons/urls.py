from django.urls import path
from .views import (
   LessonView,
   LessonListView,
   LessonCreateView
)


app_name = "lessons"
urlpatterns = [
    path("", LessonListView.as_view(), name="lesson-list"),
    path("create/", LessonCreateView.as_view(), name="lesson-create"),
    path("<int:pk>/", LessonView.as_view(), name="lesson-detail"),
]
