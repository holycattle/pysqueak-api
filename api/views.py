from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Choice, Answer, Question, ChoiceSerializer,\
    AnswerSerializer, QuestionSerializer

def get_not_implemented_message():
    return {'code':200, 'data':['Not yet implemented']}

# GET /
@api_view(['GET'])
def api_root(request, format=None):
    return Response(get_not_implemented_message())

class QuestionsView(APIView):
    def get(self, request, k, format=None):
        try:
            question = Question.objects.get(version=k)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = {
                'message': "Version doesn't exist!",
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)

class ChoicesView(APIView):
    def get(self, request, k, format=None):
        try:
            choices = Choice.objects.filter(question_id=k)
            serializer = ChoiceSerializer(choices, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = {
                'message': "Version doesn't exist!",
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)

class AnswersView(APIView):
    def post(self, request, k, format=None):
        try:
            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = {
                'message': "Version doesn't exist!",
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)