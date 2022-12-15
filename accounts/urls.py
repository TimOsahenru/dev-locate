from django.urls import path
from .views import LoginUser
from django.contrib.auth.views import LogoutView
from .views import (
    UserSignUp,
    EngineerProfile,
    EngineerSettings,
    EngineerProject,
    PrivateProjects,
    CreateMessage,
)
from . import views


urlpatterns = [
    path("", LoginUser.as_view(next_page="all_projects"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", UserSignUp.as_view(), name="signup"),
    path("profile/<str:pk>/", EngineerProfile.as_view(), name="profile"),
    path("settings/<str:pk>/", EngineerSettings.as_view(), name="settings"),
    path("projects/<str:pk>/", EngineerProject.as_view(), name="projects"),
    path("private/<str:pk>/", PrivateProjects.as_view(), name="private"),
    path("json/<str:pk>/", views.django_models_json, name="json"),
    path('message/<str:pk>/', CreateMessage.as_view(), name='message')
]
