from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Review
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializer import MerchSerializer
from .permissions import IsAdminOrReadOnly




# def index(request):
#     return render(request, 'award/index.html')


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['sitename', 'description', 'url', 'screenshot']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectListView(ListView):
    model = Project
    template_name = 'award/index.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-submitted']


class ReviewCreateView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ['design', 'usability', 'creativity', 'content']

    def dispatch(self, request, *args, **kwargs):
        """
        Overridden so we can make sure the `Project` instance exists
        before going any further.
        """
        self.project = get_object_or_404(Project, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        return super().form_valid(form)

    # def get_absolute_url(self):
    #     return reverse('project/<int:pk>/', kwargs={'pk': self.pk})


class ProjectDetailView(DetailView):
    model = Project
    

        # Rest Api create

    
class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializer = MerchSerializer(all_merch, many=True)
        return Response(serializer.data)

        
class MerchList(APIView):
#..........
    permission_classes = (IsAdminOrReadOnly,)

