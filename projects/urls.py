from django.urls import path
from .views import AllProjects, ProjectDetail, ProjectEdit, ProjectCreate, ProjectDelete


urlpatterns = [
    path('', AllProjects.as_view(), name='all_projects'),
    path('project<str:pk>/', ProjectDetail.as_view(), name='detail_project'),
    path('edit<str:pk>/', ProjectEdit.as_view(), name='edit_project'),
    path('create/', ProjectCreate.as_view(), name='create_project'),
    path('delete/<str:pk>/', ProjectDelete.as_view(), name='delete_project'),

]
