from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('breeds/', views.BreedsList.as_view(), name="breeds_list"),
    path('activitieslevel/', views.ActivityLevelList.as_view(), name="activitieslevel_list")
]
