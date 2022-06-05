from django.urls import path
from . import views

urlpatterns = [
    path("", views.analysis_index, name="analysis_index"),
    path("all_analyses/", views.analysis_all, name="analysis_all"),
    path("<int:pk>/", views.analysis_detail, name="analysis_detail"),
]