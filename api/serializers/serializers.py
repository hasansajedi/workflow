from django.http import Http404
from rest_framework import serializers
from rest_framework.status import HTTP_400_BAD_REQUEST

from api.models import Workflow, WorkflowSteps, Comment


# https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
class WorkflowStepSerializer(serializers.ModelSerializer):
    """
    Create WorkflowStep model serializer to control fields.
    """
    id = serializers.IntegerField(required=False)
    status = serializers.SerializerMethodField()

    class Meta:
        model = WorkflowSteps
        fields = ('id', 'name', 'description', 'status')

    def get_status(self, instance):
        return WorkflowSteps.STATUS_CHOICE_LIST[instance.status][1]


class CommentSerializer(serializers.ModelSerializer):
    """
    Create Comment model serializer to control fields, add new item and update item.
    """
    workflow_id = serializers.IntegerField(source='workflow_id.id', required=True)

    class Meta:
        model = Comment
        fields = ('workflow_id', 'name', 'text')

    def create(self, validated_data: dict) -> Comment:
        """
        :param validated_data: Dict type
        :return: Create an instance of Comment Model.
        """
        workflow_id = validated_data.pop('workflow_id')
        name = validated_data.pop('name')
        text = validated_data.pop('text')
        workflow = Workflow.objects.get(id=workflow_id.get("id"))
        comment = Comment.objects.create(workflow_id=workflow, name=name, text=text)

        return comment

    def update(self, instance: Comment, validated_data: dict) -> Comment:
        """
        :param instance: An instance of Comment that we want to update fields values.
        :param validated_data: Dict type
        :return: An instance of Comment Model.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.save()

        return instance


class CommentListSerializer(serializers.ModelSerializer):
    """
    Create Comment model serializer to control fields, add new item and update item.
    """

    class Meta:
        model = Comment
        fields = ('id', 'name', 'text', 'created_at', 'workflow_id')


class CommentItemSerializer(serializers.ModelSerializer):
    """
    Create Comment model serializer to control fields, add new item and update item.
    """

    class Meta:
        model = Comment
        fields = ('name', 'text', 'created_at')


class WorkflowSerializer(serializers.ModelSerializer):
    """
    Create Workflow model serializer to control fields, add new item and update item.
    """
    steps = WorkflowStepSerializer(many=True)

    class Meta:
        error_status_codes = {
            HTTP_400_BAD_REQUEST: 'Bad Request'
        }
        model = Workflow
        fields = ['name', 'description', 'steps']

    def create(self, validated_data: dict) -> Workflow:
        """
        :param validated_data: Type dict
        :return: Create an instance of Workflow Model
        """
        steps_data = validated_data.pop('steps')
        workflow, created = Workflow.objects.get_or_create(**validated_data)
        for item in steps_data:
            WorkflowSteps.objects.create(workflow_id=workflow, **item)

        return workflow

    def update(self, instance: Workflow, validated_data: dict) -> Workflow:
        """
        :param instance: An instance of Workflow that we want to update fields values.
        :param validated_data: Dict type
        :return: An instance of Workflow Model.
        """
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


class WorkflowItemSerializer(serializers.ModelSerializer):
    """
    Create Workflow model serializer to control fields, add new item and update item.
    """
    steps = WorkflowStepSerializer(many=True)
    comments = CommentItemSerializer(many=True)

    class Meta:
        error_status_codes = {
            HTTP_400_BAD_REQUEST: 'Bad Request'
        }
        model = Workflow
        fields = ['name', 'description', 'steps', 'comments']


class WorkflowListSerializer(serializers.ModelSerializer):
    """
    Create Workflow model serializer to control fields.
    """

    class Meta:
        error_status_codes = {
            HTTP_400_BAD_REQUEST: 'Bad Request'
        }
        model = Workflow
        fields = ['id', 'name', 'description', 'created_at']
