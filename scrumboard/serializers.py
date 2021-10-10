from rest_framework import serializers
from scrumboard.models import List, Card


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
