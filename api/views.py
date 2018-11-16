from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer
# Create your views here.
class MascotasView(APIView):
    def get(self,request):
        mascotas=Mascota.objects.all()
        serializer=MascotaSerializer(mascotas,many=True)
        return Response(serializer.data)