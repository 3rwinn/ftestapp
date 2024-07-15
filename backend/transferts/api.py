from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, mixins, generics
import requests

from .serializers import TransfertSerializer
from .models import Transfert


class TransfertList(generics.ListCreateAPIView):
    """
    Créer un transfert ou récuperer tous les transferts
    """

    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransfertDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Récuperer ou modifier, supprimer un transfert
    """

    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def search_client(request, keywords):
    if request.method == "GET":
        external_api_url = f'http://srv-fmetier-test:8081/api/pos/customer/search?keywords={keywords}'

        # Headers to include in the request
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        try:
            # Make a request to the external API
            response = requests.get(external_api_url, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()  # Parse the JSON response
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data, status=status.HTTP_200_OK)


def search_client_subscription(request, client_id):
    if request.method == "GET":
        external_api_url = f'http://srv-fmetier-test:8081/api/pos/customer/${client_id}/subscriptions'

        # Headers to include in the request
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        try:
            # Make a request to the external API
            response = requests.get(external_api_url, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()  # Parse the JSON response
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data, status=status.HTTP_200_OK)
