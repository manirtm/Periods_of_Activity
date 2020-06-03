from rest_framework import serializers
from .models import User, Activity_periods

class Activity_periods_serializers(serializers.ModelSerializer):
    class Meta:
        model = Activity_periods
        fields = ['start_time', 'end_time']

class User_serialize(serializers.ModelSerializer):
    activity_periods = Activity_periods_serializers(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']