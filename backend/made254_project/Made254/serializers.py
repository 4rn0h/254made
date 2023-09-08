from rest_framework import serializers
from .models import Made254

class Made254Serializer(serializers.ModelSerializer):
    class Meta:
        model = Made254
        fields = ('id', 'title', 'body',)