from django.shortcuts import render
from rest_framework.response import Response
from core.models import exchange_modal
from core.serializers import ExchangeSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from core.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated
from core.price_update import PriceUpdate
from django.http.response import JsonResponse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({        
        '/api/v1/quotes/': reverse('exchange-endpoint', request=request, format=format)
    })


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def exchange_endpoint(request):
    try:
        if request.method == 'GET':
            feed = exchange_modal.objects.all()      
            exchange_serializer = ExchangeSerializer(feed, many=True)
            return JsonResponse(exchange_serializer.data, safe=False)
        elif request.method == 'POST':
            PriceUpdate.getPriceFromExchangeSaveToDb()
            return Response("Manual Price Updated From Alphavantage",status=status.HTTP_201_CREATED)
    except Exception as e:
          return Response("ERROR!",status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#left as example
# class ExchangeList(generics.ListCreateAPIView):
#     queryset = exchange_modal.objects.all().order_by('-id')
#     serializer_class = ExchangeSerializer
#     permission_classes = [IsAuthenticated,]

#    # def perform_create(self, serializer):
#     #    serializer.save(owner=self.request.user)



         
 
    