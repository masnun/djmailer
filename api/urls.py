from rest_framework.routers import SimpleRouter

from .views import SubscriberViewSet

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)

urlpatterns = router.urls
