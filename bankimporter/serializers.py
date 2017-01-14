from rest_framework import serializers
from bankimporter.models import RealTransaction, Tag



class RealTransacitonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RealTransaction
        fields = ['id','date', 'value', 'payment_type', 'main_tag', 'tags']



class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['name',]
