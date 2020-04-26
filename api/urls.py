from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.schemas import get_schema_view

from . import views

app_name = "api"

urlpatterns = [
    re_path(r'^workflow/(?P<pk>[0-9]+)$',  # Url to get update or delete a movie
            views.WorkflowGetDeleteUpdate.as_view(),
            name='WorkflowGetDeleteUpdate'
            ),
    path('workflow/',  # urls list all and create new one
         views.WorkflowListPost.as_view(),
         name='WorkflowListPost'
         ),
    path('comment/',  # urls list all and create new one
         views.CommentListPost.as_view(),
         name='CommentListPost'
         ),
    re_path(r'^comment/(?P<pk>[0-9]+)$',  # Url to get update or delete a movie
            views.CommentGetDeleteUpdate.as_view(),
            name='CommentGetDeleteUpdate'
            ),
]
