from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer

class TeamListView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class PersonListView(APIView):
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
