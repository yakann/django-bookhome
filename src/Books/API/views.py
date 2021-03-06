from django.shortcuts import render
from .serializers import BookSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.

class KitapListesi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'kitaplarlistesi.html'
    def get(self, request):
            queryset = Books.objects.all()
            serializer = BookSerializers(queryset, many=True)
            return Response({'serializer':serializer, 'queryset':queryset})
    def post(self, request):
            serializer = BookSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KitapDetay(APIView):

    def get_object(self, id):
        try:
            return Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = BookSerializers(queryset)
        return Response({'serializer':serializer, 'queryset':queryset})

    def put(self, request):
        cari = self.get_object(id)
        serializer = BookSerializers(cari, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        cari = self.get_object(id)
        cari.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
