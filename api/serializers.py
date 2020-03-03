from rest_framework.serializers import ModelSerializer
from django.db import models

from wiki.models import Question, Choice

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'