from urllib.request import Request

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .models import Workflow, Comment
from api.utils.pagination import CustomPagination
from .serializers.serializers import WorkflowSerializer, CommentSerializer


class WorkflowListPost(GenericAPIView):
    """
    To perform List and Create actions on Workflow Model.

    Methods
    -------
    get
        Return a list of all created Workflow.
    post
        Create a Workflow instance.
    """

    serializer_class = WorkflowSerializer
    pagination_class = CustomPagination
    queryset = Workflow.objects.all()

    def get(self, request: Request, format=None) -> Response:
        """
        List all created workflows.

        Parameters
        ----------
        request : Request
            HTTP GET request
        format : str, optional
            Format for the rendered response (the default is None)
        Returns
        -------
        Response
            Return the response with all serialized workflows
        """
        workflows = Workflow.objects.all()
        paginate_queryset = self.paginate_queryset(workflows)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, format=None) -> Response:
        """
        Create a workflow instance.
        
        Parameters
        ----------
        request : Request
            HTTP POST request
        format : str, optional
            Format for the rendered response (the default is None)
        Returns
        -------
        Response
            Return the response with the created serialized workflow
        """

        serializer = WorkflowSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkflowGetDeleteUpdate(GenericAPIView):
    """
    To perform Retrieve, Update or delete an instance of Workflow Model.

    Methods
    -------
    get
        Return a serialized Workflow.
    put
        Update a workflow instance.
    delete
        Delete a workflow instance.
    Raises
    ------
    Http404
        HTTP error if the Workflow doesn't exist
    """

    serializer_class = WorkflowSerializer
    queryset = Workflow.objects.all()

    def get_object(self, pk: int) -> Workflow:
        """
        Get the Workflow object.
        Parameters
        ----------
        pk: integer
            Identifier of the Workflow
        Raises
        ------
        Http404
            Return HTTP 404 error code if the object doesn't exist
        Returns
        -------
        dict
            Dictionary of the query result
        """
        try:
            return Workflow.objects.get(pk=pk)
        except Workflow.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int, format=None) -> Response:
        """
        Obtain a workflow instance.
        Parameters
        ----------
        request: Request
            HTTP GET request
        id: str
            Identifier of the Workflow
        format: str, optional
            Format for the rendered response (the default is None)
        Raises
        ------
        PermissionDenied
            Return HTTP 403 error code if the user is denied
        Returns
        -------
        Response
            Return the response with the serialized workflow
        """

        workflow = self.get_object(pk)
        if isinstance(workflow, Workflow):
            serializer = WorkflowSerializer(workflow)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None) -> Response:
        """
        Update a workflow instance.

        Parameters
        ----------
        request : Request
            HTTP GET request
        id : str
            Identifier of the Workflow
        format : str, optional
            Format for the rendered response (the default is None)
        Raises
        ------
        PermissionDenied
            Return HTTP 403 error code if the user is denied
        Returns
        -------
        Response
            Return the response with the serialized workflow
        """
        workflow = self.get_object(pk)

        serializer = WorkflowSerializer(workflow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None) -> Response("", status.HTTP_204_NO_CONTENT):
        """
        Delete a workflow instance.

        Parameters
        ----------
        request : Request
            HTTP GET request
        pk : str
            Identifier of the Workflow
        format : str, optional
            Format for the rendered response (the default is None)
        Raises
        ------
        PermissionDenied
            Return HTTP 403 error code if the user is denied
        Returns
        -------
        Response
            Return the response with the result code of the deletion
        """
        workflow = self.get_object(pk)
        if workflow is not None:
            workflow.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        raise Http404


class CommentListPost(GenericAPIView):
    """
    To perform List and Create actions on Comment Model.

    Methods
    -------
    get
        Return a list of all created Comment.
    post
        Create a Comment instance.
    """
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    queryset = Comment.objects.all()

    def get(self, request: Request, format=None) -> Response:
        """
        List all created comments.

        Parameters
        ----------
        request : Request
            HTTP GET request
        format : str, optional
            Format for the rendered response (the default is None)
        Returns
        -------
        Response
            Return the response with all serialized comments
        """
        comments = Comment.objects.all()
        paginate_queryset = self.paginate_queryset(comments)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request: Request, format=None) -> Response:
        """
        Create a comment instance.

        Parameters
        ----------
        request : Request
            HTTP POST request
        format : str, optional
            Format for the rendered response (the default is None)
        Returns
        -------
        Response
            Return the response with the created serialized comment
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentGetDeleteUpdate(GenericAPIView):
    """
    To perform Retrieve, Update or delete an instance of Comment Model.

    Methods
    -------
    get
        Return a serialized comment.
    put
        Update a comment instance.
    delete
        Delete a comment instance.
    Raises
    ------
    Http404
        HTTP error if the comment doesn't exist
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_object(self, pk: int) -> Comment:
        """
        Get the Comment object.
        Parameters
        ----------
        pk: integer
            Identifier of the Comment
        Raises
        ------
        Http404
            Return HTTP 404 error code if the object doesn't exist
        Returns
        -------
        dict
            Dictionary of the query result
        """
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int, format=None) -> Response:
        """
        Obtain a comment instance.
        Parameters
        ----------
        request: Request
            HTTP GET request
        id: str
            Identifier of the comment
        format: str, optional
            Format for the rendered response (the default is None)
        Raises
        ------
        PermissionDenied
            Return HTTP 403 error code if the user is denied
        Returns
        -------
        Response
            Return the response with the serialized comment
        """
        comment = self.get_object(pk)
        if isinstance(comment, Comment):
            serializer = self.serializer_class(comment)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None) -> Response:
        """
        Update a comment instance.

        Parameters
        ----------
        request : Request
            HTTP GET request
        id : str
            Identifier of the comment
        format : str, optional
            Format for the rendered response (the default is None)
        Raises
        ------
        PermissionDenied
            Return HTTP 403 error code if the user is denied
        Returns
        -------
        Response
            Return the response with the serialized comment
        """
        comment = self.get_object(pk)

        serializer = self.serializer_class(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response("", status.HTTP_204_NO_CONTENT):
        """
        Delete a comment instance.

        Parameters
        ----------
        request : Request
            HTTP GET request
        pk : str
            Identifier of the comment
        format : str, optional
            Format for the rendered response (the default is None)
        Raises
        ------
        PermissionDenied
            Return HTTP 403 error code if the user is denied
        Returns
        -------
        Response
            Return the response with the result code of the deletion
        """
        comment = self.get_object(pk)
        if comment is not None:
            comment.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        raise Http404
