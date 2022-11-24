from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Team
from django.forms.models import model_to_dict

class TeamView(APIView):
    def post(self, request):
        team = Team.objects.create(**request.data)

        return Response(model_to_dict(team), status.HTTP_201_CREATED)


    def get(self, request):
        return Response(Team.objects.all().values())