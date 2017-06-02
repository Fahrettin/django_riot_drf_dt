from rest_framework import serializers
from app.models import Staff

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('name', 'position', 'office', 'age', 'startdate')

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        instance.office = validated_data.get('office', instance.office)
        instance.age = validated_data.get('age', instance.age)
        instance.startdate = validated_data.get('startdate', instance.startdate)
        instance.save()
        return instance
