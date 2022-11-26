from django.urls import path
from .views import LoginUser
from django.contrib.auth.views import LogoutView
from .views import UserSignUp, EngineerProfile, EngineerSettings


urlpatterns = [
    path('', LoginUser.as_view(next_page='all_projects'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('profile/<str:pk>/', EngineerProfile.as_view(), name='profile'),
    path('settings/<str:pk>/', EngineerSettings.as_view(), name='settings')
]
