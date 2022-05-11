from statistics import mode
from django_filters import rest_framework as filters
from .models import Offer



class OfferFilter(filters.FilterSet, filters.OrderingFilter):
    rate_min = filters.RangeFilter()
    rate_max = filters.RangeFilter()
    payment_min= filters.RangeFilter()
    payment_max = filters.RangeFilter()

    # order=
    # price=
    # deposit=
    # term=
    class Meta:
        model = Offer
        fields = ['rate_min', 'rate_max', 'payment_min', 'payment_max']
        ordering_fields = ['payment']
        