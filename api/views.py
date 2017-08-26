from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Choice, Answer, ChoiceSerializer, AnswerSerializer

def get_not_implemented_message():
    return {'code':200, 'data':['Not yet implemented']}

# GET /
@api_view(['GET'])
def api_root(request, format=None):
    return Response(get_not_implemented_message())

class ChoicesView(APIView):
    def get(self, request, id, format=None):
        try:
            choices = Choice.objects.filter(version=pk)
            serializer = ChoiceSerializer(choices, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            data = {
                'message': "Version doesn't exist!",
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)
