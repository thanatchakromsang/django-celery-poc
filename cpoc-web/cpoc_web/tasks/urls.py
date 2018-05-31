from django.conf.urls import url

from tasks.views import Task


urlpatterns = [
    url(r'^$', Task.as_view(), name='tasks'),
    # url(r'^customers/(?P<id>.+)/$', CustomersDetailView.as_view(), name='customers_detail'),
]
