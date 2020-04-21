from rest_framework import serializers

from api.models import Workflow, WorkflowSteps


# Serializers define the API representation.
class WorkflowSerializer(serializers.ModelSerializer):
    steps = serializers.StringRelatedField(many=True)
    class Meta:
        model = Workflow
        fields = ['Workflow_name', 'description', 'steps']

    # name = serializers.CharField(required=True, allow_blank=False, max_length=150)
    # description = serializers.CharField(required=True, allow_blank=False, max_length=250)

    def create(self, validated_data):
        return Workflow.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

