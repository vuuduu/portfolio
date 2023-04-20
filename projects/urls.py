# Hold all the url configuration for the projects apps
# https:.../projects/
from django.urls import path
from . import views

# 2nd path: dynamically generating the url depend on which project you want to view.
urlpatterns = [
    path("", views.project_index, name="project_index"), # home for projects app
    path("<int:pk>/", views.project_detail, name="project_detail"), # projects/1,2,3.../
]