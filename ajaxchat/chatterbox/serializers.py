from rest_framework import serializers
from .models import Statement

class StatementSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Statement
        fields = ('text', 'created')
