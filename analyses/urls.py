from django.urls import path
from . import views

urlpatterns = [
    path("", views.analysis_index, name="analysis_index"),
    path("all_analyses/", views.analysis_all, name="analysis_all"),
    path("<int:pk>/", views.analysis_detail, name="analysis_detail"),
    path("question", views.get_answer, name="question"),
    path("ask_ai", views.get_answer, name="ask_ai"),
    path("active_learner_labeling_app", views.get_active_learner, name="active_learner"),
]
