from typing import List
from urllib.request import Request

from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Workflow, Comment
from .pagination import CustomPagination
from .serializers import WorkflowSerializer, CommentSerializer


class WorkflowGetDeleteUpdate(RetrieveUpdateDestroyAPIView):
    """
    To perform Retrieve, Update and Destroy an instance of Workflow Model.
    """
    serializer_class = WorkflowSerializer

    def get_queryset(self, pk: int) -> Workflow:
        """
        Create queryset of item Workflow Model by primary key.
        :param pk: Primary key value of Workflow Model that we want get item.
        :return: An instance of Workflow Model.
        """
        try:
            workflow = Workflow.objects.get(pk=pk)
        except Workflow.DoesNotExist:
            raise Http404()
        return workflow

    def get(self, request: Request, pk: int) -> Response:
        """
        Get a workflow by id.
        :param pk: Primary key value of workflow Model that we want to retrieve.
        :return: Serialized workflow instance after retrieved.
        """
        workflow = self.get_queryset(pk)
        if isinstance(workflow, Workflow):
            serializer = WorkflowSerializer(workflow)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """
        Update a workflow object.
        :param pk: Primary key value of workflow Model that we want to update.
        :return: Serialized instance after updated item values.
        """
        workflow = self.get_queryset(pk)

        serializer = WorkflowSerializer(workflow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response("", status.HTTP_204_NO_CONTENT):
        """
        Delete a workflow.
        :param pk: Primary key value of workflow Model that we want to delete.
        :return: Response as String to show item deleted.
        """
        workflow = self.get_queryset(pk)

        workflow.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class WorkflowListPost(ListCreateAPIView):
    """
    To perform List and Create actions on Workflow Model.
    """
    serializer_class = WorkflowSerializer
    pagination_class = CustomPagination

    def get_queryset(self) -> List[Workflow]:
        """
        Create queryset of item Workflow Model.
        :return: An instance of List of workflows.
        """
        workflows = Workflow.objects.all()
        return workflows

    def get(self, request: Request) -> Response:
        """
        Get all workflows.
        :return: Serialized instance of all workflows.
        """
        workflows = self.get_queryset()
        paginate_queryset = self.paginate_queryset(workflows)
        serializer = self.serializer_class(paginate_queryset, many=True)
        print(serializer.data)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Create a new workflow
        :return: An instance of Workflow Model.
        """
        serializer = WorkflowSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListPost(ListCreateAPIView):
    """
    To perform List and Create actions on Comment Model.
    """
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> List[Comment]:
        """
        Create queryset of item Comment Model.
        :return: An instance of List of Comments.
        """
        comments = Comment.objects.all()
        return comments

    def get(self, request: Request) -> Response:
        """
        Get all comments.
        :return: Serialized instance of all comments.
        """
        comments = self.get_queryset()
        paginate_queryset = self.paginate_queryset(comments)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Create a new comment.
        :return: An instance of Comment Model.
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentGetDeleteUpdate(RetrieveUpdateDestroyAPIView):
    """
    To perform Retrieve, Update and Destroy an instance of Comment Model.
    """
    serializer_class = CommentSerializer

    def get_queryset(self, pk: int) -> Comment:
        """
        Create queryset of item Comment Model by primary key.
        :param pk: Primary key value of Comment Model that we want get item.
        :return: An instance of Comment Model.
        """
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404()
        return comment

    def get(self, request: Request, pk: int) -> Response:
        """
        Get a comment by id.
        :param pk: Primary key value of Comment Model that we want to retrieve.
        :return: Serialized instance after retrieved.
        """
        comment = self.get_queryset(pk)
        if isinstance(comment, Comment):
            serializer = self.serializer_class(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        """
        Update a comment object.
        :param pk: Primary key value of Comment Model that we want to update.
        :return: Serialized instance after updated item values.
        """
        comment = self.get_queryset(pk)

        serializer = self.serializer_class(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response("", status.HTTP_204_NO_CONTENT):
        """
        Delete a comment.
        :param pk: Primary key value of Comment Model that we want to delete.
        :return: Response as String to show item deleted.
        """
        comment = self.get_queryset(pk)

        comment.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
