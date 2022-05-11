from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .service import OfferFilter
from .models import Offer
from .serializers import OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, )
    filterset_class = OfferFilter

    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get_queryset(self):
        offers = Offer.objects.all()
        price = self.request.query_params.get('price') # s
        deposit = self.request.query_params.get('deposit') #-s
        term = self.request.query_params.get('term') # m

        # x = S*p / 1-(1+p)*(1-m)
        for offer in offers:
            offer.payment = int(((int(price)-int(deposit)) * float(offer.rate_min)) / (1 - (1+float(offer.rate_min)) * (1-int(term))))
            print(offer.payment)
        return offers

