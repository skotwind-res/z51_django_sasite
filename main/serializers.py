from rest_framework import serializers
from .models import CommonInfo


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonInfo
        fields = ('id', 'title', 'content', 'price', 'rubric')
