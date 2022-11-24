from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Team
from django.forms.models import model_to_dict

class TeamCreateView(APIView):
    def post(self, request):
        team = Team.objects.create(**request.data)

        return Response(model_to_dict(team), status.HTTP_201_CREATED)


    def get(self, request):
        return Response(Team.objects.all().values())


class TeamView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        
        return Response(model_to_dict(team))


    def patch(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)


        for key, value in request.data.items():
            setattr(team, key, value)


        team.save()

        return Response(model_to_dict(team), status.HTTP_200_OK)


    def delete(self, request, team_id):
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)