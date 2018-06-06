from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.tasks import create_random_word


class TaskAView(APIView):
    def get(self, request):
        create_random_word.apply_async()
        return Response({
            'status': 1
        })
