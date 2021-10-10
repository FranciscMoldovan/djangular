from scrumboard.api import CardViewSet, ListViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter() # insteadd of urlpatterns list
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

# calling a bad URL shows a lot of URLS created automatically
urlpatterns = router.urls
