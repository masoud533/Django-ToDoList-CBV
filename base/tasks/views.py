# tasks/views.py
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Task
from .forms import TaskCreateForm
from django.views import View

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



class TaskToggleDoneView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.is_done = not task.is_done
        task.save()
        return redirect('tasks:list')
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('title',)
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        # امنیت: فقط تسک‌های خود یوزر
        return Task.objects.filter(user=self.request.user)
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)