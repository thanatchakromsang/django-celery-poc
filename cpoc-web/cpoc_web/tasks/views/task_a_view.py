from rest_framework.response import Response
from rest_framework.views import APIView


class TaskAView(APIView):
    def get(self, request):
        return Response({
            'status': 1
        })



