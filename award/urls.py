from . import views 
from django.urls import path
from django.conf.urls import url
from .views import  ProjectCreateView  

#, ProjectUpdateView, ProjectDeleteView, ProjectListView, ProjectDetailView


urlpatterns = [
    path('', views.index, name='home'),
    path('Project/new/', ProjectCreateView.as_view(), name='Project-create'),

]