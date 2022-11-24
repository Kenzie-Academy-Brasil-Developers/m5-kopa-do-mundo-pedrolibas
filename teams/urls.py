from django.urls import path
from .views import TeamCreateView, TeamView

urlpatterns = [
    path("teams/", TeamCreateView.as_view()),
    path("teams/<int:team_id>/", TeamView.as_view())
]