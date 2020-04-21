from django.urls import path

from .views import WorkflowView


app_name = "api"

urlpatterns = [
    path('', WorkflowView.as_view()),
]
