from django.conf.urls import url

from tasks.views.task_a_view import TaskAView
from tasks.views.task_a_periodic_view import TaskAPeriodicView
from tasks.views.task_b_view import TaskBView
from tasks.views.task_b_periodic_view import TaskBPeriodicView


urlpatterns = [
    url(r'^task_a/$', TaskAView.as_view(), name='task_a'),
    url(r'^task_a_periodic/$', TaskAPeriodicView.as_view(), name='task_a_periodic'),
    url(r'^task_b/$', TaskBView.as_view(), name='task_b'),
    url(r'^task_b_periodic/$', TaskBPeriodicView.as_view(), name='task_b_periodic'),
]
