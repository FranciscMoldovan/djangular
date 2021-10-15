from rest_framework.viewsets import ModelViewSet
from scrumboard.serializers import ListSerializer, CardSerializer
from scrumboard.models import List, Card
from rest_framework import permissions

"""
ModelViewSet allows GET PUT POST DELETE
in older commits it was smth else
"""


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated, )


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)

