from django.shortcuts import render
from .models import File, Update, Blocked, Data
from .serializers import FileListSerializers, UpdateListSerializers, BlockedListSerializers, DataListSerializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics



class FileDetailsAPIView(APIView):
    def get(self, request, format=None):
        ovpn_fil = File.objects.all()
        serialize = FileListSerializers(ovpn_fil, many = True)
        data = {'ovpn_file': serialize.data}
        return Response(data, status=status.HTTP_201_CREATED)

class AppDetailsAPIView(APIView):
    def get(self, request, format=None):
        ads = True
        update = Update.objects.all()
        blocked = Blocked.objects.all()
        data = Data.objects.all()
        update_serialize = UpdateListSerializers(update, many = True)
        blocked_serialize = BlockedListSerializers(blocked, many = True)
        data_serialize = DataListSerializers(data, many = True)
        data = {'ads': ads, 'update': update_serialize.data, 'blocked': blocked_serialize.data, 'data': data_serialize.data}
        return Response(data, status=status.HTTP_201_CREATED)




