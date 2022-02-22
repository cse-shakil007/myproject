from rest_framework import serializers
from .models import File, Update, Blocked, VIP,Free, Data

class FileListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'file')

class UpdateListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Update
        fields = ('version', 'title','description', 'size')

class BlockedListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blocked
        fields = ('id', 'apps')

class VIPListSerializers(serializers.ModelSerializer):
    class Meta:
        model = VIP
        fields = '__all__'
        read_only_fields = ['id']

class FreeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Free
        fields = '__all__'
        read_only_fields = ['id']

class DataListSerializers(serializers.ModelSerializer):
    #vip = VIPListSerializers(read_only=True)
    vip = VIPListSerializers(many=True)
    free = FreeListSerializers(many=True)
    class Meta:
        model = Data
        fields = ('id', 'city', 'vip', 'free')
        read_only_fields = ['id']

