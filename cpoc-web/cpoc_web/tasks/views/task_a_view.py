from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from tasks.tasks import create_random_word


class TaskAView(APIView):
    def get(self, request):
        return Response({
            'status': 1
        })
