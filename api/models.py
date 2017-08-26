from django.db import models
from rest_framework import serializers

class Question(models.Model):
    version = models.CharField(primary_key=True, max_length=8)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Choice(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class Answer(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_id = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class ChoiceSerializer(serializers.ModelSerializer):
    version = serializers.SerializerMethodField('get_version_from_question')
    class Meta:
        model = Choice
        fields = ('id', 'text', 'version', 'created_on', 'updated_on',)

    def get_version_from_question(self, obj):
        return obj.question_id

class QuestionSerializer(serializers.ModelSerializer):
    # TODO: create a serializer that returns list of choices for the question
    class Meta:
        model = Question
        fields = ('text', 'version', 'created_on', 'updated_on',)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'choice_id', 'user_id', 'created_on',)
