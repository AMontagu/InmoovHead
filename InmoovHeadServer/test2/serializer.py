from rest_framework import serializers
from test2.models import *


class RobotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Robot
        fields = ('name', 'serialNumer')


