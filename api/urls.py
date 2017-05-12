from django.conf.urls import url

from .views import hello_world

urlpatterns = [
    url(r'^hello', hello_world, name="hello_world")
]
