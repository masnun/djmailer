from rest_framework.viewsets import ModelViewSet

from .serializers import SubscriberSerializer
from .models import Subscriber


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
