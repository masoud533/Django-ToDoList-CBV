# tasks/views.py
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskCreateForm


class TaskListView(LoginRequiredMixin, FormMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return super().get(request, *args, **kwargs)

