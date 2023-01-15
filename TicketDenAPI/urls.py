from rest_framework.routers import DefaultRouter
from .views import EventViewSet

app_name = 'TicketDenAPI'

router = DefaultRouter()
router.register('', EventViewSet, basename='events')
urlpatterns = router.urls

# urlpatterns = [
#     #path("admin/", admin.site.urls),
# ]