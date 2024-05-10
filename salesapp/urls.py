from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('run-pipeline/', views.run_pipeline, name='run_pipeline'),
    path('run-pipelinee/', views.run_pipelinee, name='run_pipelinee'),
]
