from rest_framework.routers import SimpleRouter
from django.conf.urls import url

from .views import SubscriberViewSet, login

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = router.urls + [
    url(r'^jwt-auth/', obtain_jwt_token),
]
