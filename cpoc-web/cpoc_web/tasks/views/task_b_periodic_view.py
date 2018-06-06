from rest_framework.response import Response
from rest_framework.views import APIView
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class TaskBPeriodicView(APIView):
    def get(self, request):
        schedule, create = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
        )
        PeriodicTask.objects.create(
            interval=schedule,
            name='TaskPeriodicB',
            task='tasks.tasks.create_random_word_long',
        )
        return Response({
            'status': 1
        })
