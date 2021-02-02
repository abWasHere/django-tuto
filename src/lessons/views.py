from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views import View

from .models import Lesson
from .forms import LessonModelForm


# CLASS BASED VIEWS != function based views


class LessonCreateView(View):
    template_name = "lessons/lesson_create.html"

    def get(self, request, *args, **kwargs):
        # GET method
        form = LessonModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = LessonModelForm(request.POST)
        context = {"form": form}
        if form.is_valid():
            form.save()
            form = LessonModelForm()
        return render(request, self.template_name, context)


class LessonView(View):
    template_name = "lessons/lesson_detail.html"

    def get(self, request, pk=None, *args, **kwargs):
        id_ = pk
        context = {}
        if id_ is not None:
            obj = get_object_or_404(Lesson, id=id_)
            context = {"object": obj}

        return render(request, self.template_name, context)


class LessonListView(View):
    template_name = "lessons/lesson_list.html"
    queryset = Lesson.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {"object_list": self.get_queryset()}
        return render(request, self.template_name, context)
