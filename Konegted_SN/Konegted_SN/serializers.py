from rest_framework import serializers
from .models import *


class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = '_all_'
        # read_only_fields  = 'telephone',


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '_all_'
        # read_only_fields  = 'telephone',
        # depth = 1


class MatierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matier
        fields = '_all_'
