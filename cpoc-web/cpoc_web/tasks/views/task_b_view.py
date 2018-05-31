from rest_framework.response import Response
from rest_framework.views import APIView


class TaskBView(APIView):
    def get(self, request):
        return Response({
            'status': 1
        })



