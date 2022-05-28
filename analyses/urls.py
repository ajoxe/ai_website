from django.urls import path
from . import views

urlpatterns = [
    path("", views.analysis_index, name="analysis_index"),
    path("<int:pk>/", views.analysis_detail, name="analysis_detail"),
]