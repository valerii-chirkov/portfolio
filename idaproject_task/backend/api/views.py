from rest_framework.decorators import api_view
from rest_framework.response import Response

from offers.models import Offer
from offers.serializers import OfferSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = OfferSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)
