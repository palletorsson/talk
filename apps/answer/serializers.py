from django.forms import widgets
from rest_framework import serializers
from models import Answers


class AnswersSerializer(serializers.Serializer):
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    question  = serializers.CharField(required=False,
                                  max_length=255)
    answer  = serializers.CharField(required=False,
                                  max_length=255)


    def restore_object(self, attrs, instance=None):

        if instance:
            instance.question = attrs.get('question', instance.question)
            instance.answer = attrs.get('question', instance.answer)
            return instance

        # Create new instance
        return Answers(**attrs)


