from bankimporter.serializers import RealTransacitonSerializer, TagSerializer
from bankimporter.models import RealTransaction, Tag
from rest_framework import viewsets


class RealTransactionViewSet(viewsets.ModelViewSet):
    '''API for modifing transactions'''
    queryset = RealTransaction.objects.all().order_by('-date')
    serializer_class = RealTransacitonSerializer


class TagViewSet(viewsets.ModelViewSet):
    '''API for modifing transactions'''
    queryset = Tag.objects.all().order_by('-date')
    serializer_class = TagSerializer
