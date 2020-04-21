from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Workflow


class WorkflowView(APIView):
    def get(self, request):
        workflow = Workflow.objects.all()
        return Response({"workflows": workflow})
