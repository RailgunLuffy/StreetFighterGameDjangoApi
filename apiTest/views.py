from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication 

from .models import Player
from .serializers import PlayerSerializer

# Create your views here.

class PlayerApiView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def get(self, request, format=None,*args, **kwargs):
        # players = Player.objects.order_by('-id')[:1]
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None, *args, **kwargs):
        data = {
            'player1Hp': request.data.get('player1Hp'),
            'player2Hp': request.data.get('player2Hp')
        }
        serializer = PlayerSerializer(data=data)
        # print(data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getLastPlayerApiView(APIView):
    def get(self, request, *args, **kwargs):
        players = Player.objects.order_by('-id')[:1]
        serializer = PlayerSerializer(players, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)