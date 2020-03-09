from rest_framework import serializers
from .models import School, Coach



class CoachSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Coach
		fields = ('short_name', 'name', 'position', 'imageUrl')

class SchoolSerializer(serializers.ModelSerializer):
	teacher_v2 = CoachSerializer()
	class Meta:
		model = School
		fields = ('name', 'description', 'place', 'teacher',  'startTime', 'endTime', 'weekDay', 'servise_id', 'teacher_v2', 'color')



