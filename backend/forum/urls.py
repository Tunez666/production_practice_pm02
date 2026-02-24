from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TopicViewSet, PostViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls