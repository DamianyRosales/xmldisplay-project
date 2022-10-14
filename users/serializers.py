from rest_framework.serializers import ModelSerializer
from .models import Tab

class TabSerializer(ModelSerializer):
    class Meta:
        model = Tab
        fields = '__all__'
