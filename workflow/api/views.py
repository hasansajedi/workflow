from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Workflow, WorkflowSteps
from .pagination import CustomPagination
from .serializers import WorkflowSerializer


class get_delete_update_workflow(RetrieveUpdateDestroyAPIView):
    serializer_class = WorkflowSerializer

    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            workflow = Workflow.objects.get(pk=pk)
        except Workflow.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return workflow

    # Get a workflow
    def get(self, request, pk):
        workflow = self.get_queryset(pk)
        serializer = WorkflowSerializer(workflow)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a workflow
    def put(self, request, pk):
        workflow = self.get_queryset(pk)

        serializer = WorkflowSerializer(workflow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a workflow
    def delete(self, request, pk):
        workflow = self.get_queryset(pk)

        workflow.delete()
        content = {
            'status': 'NO CONTENT'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class get_post_workflow(ListCreateAPIView):
    serializer_class = WorkflowSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        workflows = Workflow.objects.all()
        return workflows

    # Get all workflows
    def get(self, request):
        workflows = self.get_queryset()
        paginate_queryset = self.paginate_queryset(workflows)
        serializer = self.serializer_class(paginate_queryset, many=True)
        print(serializer.data)
        return self.get_paginated_response(serializer.data)

    # Create a new workflow
    def post(self, request):
        serializer = WorkflowSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
