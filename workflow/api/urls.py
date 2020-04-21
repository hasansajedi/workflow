from django.urls import path, re_path
from django.conf.urls import include, url
from rest_framework import routers

from . import views

app_name = "api"

urlpatterns = [
    re_path(r'^workflow/(?P<pk>[0-9]+)$',  # Url to get update or delete a movie
            views.get_delete_update_workflow.as_view(),
            name='get_delete_update_workflow'
            ),
    path('workflow/',  # urls list all and create new one
         views.get_post_workflow.as_view(),
         name='get_post_workflows'
         )
]
