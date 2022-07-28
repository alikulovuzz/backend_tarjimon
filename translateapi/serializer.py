

from rest_framework import serializers

from translateapi.models import Translate


class TranslateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translate
        fields = ('text', 'from_lang', 'to_lang', 'result','izox')
