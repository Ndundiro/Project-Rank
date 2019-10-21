from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def index(request):
#     return render(request, 'award/index.html')



class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['sitename', 'description', 'url', 'screenshot']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})


class ProjectListView(ListView):
    model = Project
    template_name = 'award/index.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-submitted']


class ReviewCreateView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ['design', 'usability', 'creativity', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('', kwargs={'pk': self.pk})



class ProjectDetailView(DetailView):
    model = Project


# class ReviewListView(ListView):
#     model = Review
#     template_name = 'award/reviews.html'  #<app>/<model>_<viewtype>.html
#     context_object_name = 'reviews'
#     ordering = ['-submitted']


