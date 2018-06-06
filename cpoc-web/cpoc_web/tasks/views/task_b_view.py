from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.tasks import create_random_word_long


class TaskBView(APIView):
    def get(self, request):
        create_random_word_long.apply_async()
        return Response({
            'status': 1
        })
