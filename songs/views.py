from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Song
# Create your views here.

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields= '__all__'

@api_view(['GET'])
def Home(request):
  songs = Song.objects.all()
  serializer = SongSerializer(songs,many=True)
  return Response(serializer.data)