from scrumboard.api import CardViewSet, ListViewSet
from rest_framework.routers import DefaultRouter

"""
DefaultRouter class allows automatic routing of 
ALL URLS for all operations on object from DB
ViewSet is mapped with Router below in code.
Finally, urlpatterns gets populated
"""

router = DefaultRouter() # insteadd of urlpatterns list
router.register(r'lists', ListViewSet)
router.register(r'cards', CardViewSet)

# calling a bad URL shows a lot of URLS created automatically
urlpatterns = router.urls
