import os
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', '')
    if codespace_name:
        api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        api_url = "http://localhost:8000/api/"
    return JsonResponse({"api_url": api_url})

urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
