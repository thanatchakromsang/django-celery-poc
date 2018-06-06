from rest_framework.response import Response
from rest_framework.views import APIView
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class TaskAPeriodicView(APIView):
    def get(self, request):
        schedule, create = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name='TaskPeriodicA',
            task='tasks.tasks.create_random_word',
        )
        return Response({
            'status': 1
        })
