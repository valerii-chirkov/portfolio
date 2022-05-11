from rest_framework import serializers

from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    payment = serializers.IntegerField(default=None, read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'