from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, 'award/index.html')



class ProjectCreateView(CreateView):
    model = Project
    fields = ['sitename', 'description', 'url', 'screenshot']

    def form_valid(self, form):
        form.instance.ser = self.request.user
        return super().form_valid(form)
