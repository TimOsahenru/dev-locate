from django.urls import path
from .views import CreateMessage


urlpatterns = [
    path("<str:pk>/", CreateMessage.as_view(), name="create-message")
]
