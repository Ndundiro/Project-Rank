from . import views 
from django.urls import path
from django.conf.urls import url
from .views import  ProjectCreateView, ProjectListView, ReviewCreateView, ProjectDetailView

#, ProjectUpdateView, ProjectDeleteView, ProjectDetailView


urlpatterns = [
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('', ProjectListView.as_view(), name='index'),
    path('review/new/<int:pk>/', ReviewCreateView.as_view(), name='review-create'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

     # path('', views.index, name='home'),

]