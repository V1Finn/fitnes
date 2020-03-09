from django.http import JsonResponse
from django.shortcuts import render
from .models import School, Coach
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SchoolSerializer, CoachSerializer

@api_view(['GET'])
def get_rest(request, servise_id):
	if request.method == 'GET':
		schools = School.objects.filter(servise_id=servise_id)
		serialized =SchoolSerializer(schools, many=True)
		return Response(serialized.data)
		


def index(request):

	return render(request, 'rest/index.html')

