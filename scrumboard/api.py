from rest_framework.generics import ListAPIView
from scrumboard.serializers import ListSerializer, CardSerializer
from scrumboard.models import List, Card


class ListApi(ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardApi(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

