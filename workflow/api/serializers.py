from django.http import Http404
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from api.models import Workflow, WorkflowSteps


# https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
class WorkflowStepSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = WorkflowSteps
        fields = ('id', 'name', 'description')


class WorkflowSerializer(serializers.ModelSerializer):
    steps = WorkflowStepSerializer(many=True)

    class Meta:
        model = Workflow
        fields = ['name', 'description', 'steps']

    def create(self, validated_data):
        steps_data = validated_data.pop('steps')
        workflow, created = Workflow.objects.get_or_create(**validated_data)
        for item in steps_data:
            WorkflowSteps.objects.create(workflow_id=workflow, **item)

        return workflow

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        steps = validated_data.get('steps')
        workflowSteps = WorkflowSteps.objects.filter(workflow_id=instance)

        workflowSteps_ids = [WorkflowSteps.objects.get(id=x.id).id for x in workflowSteps]
        steps_ids = [x.get('id') for x in steps]
        if set(steps_ids) == set(workflowSteps_ids):
            for item in steps:
                _id = item.get('id', None)
                if _id:
                    try:
                        step_item = WorkflowSteps.objects.get(id=_id, workflow_id=instance)
                        step_item.name = item.get('name', step_item.name)
                        step_item.description = item.get('description', step_item.description)
                        step_item.save()
                    except WorkflowSteps.DoesNotExist:
                        raise Http404("WorkflowSteps does not exist.")
                else:
                    WorkflowSteps.objects.create(workflow_id=instance, **item)

        return instance
