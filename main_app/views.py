from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data
class Breed:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description


breeds = [
  Breed ("Little Spokane River", "https://assets.change.org/photos/9/lq/sr/HuLQsrEXlyAdApc-1600x900-noPad.jpg?1622402845",
          "Blah"),
  Breed ("Heyburn State Park",
          "https://lh3.googleusercontent.com/p/AF1QipOheBfE-Bixtqcbm3zw5N_wif3JiDaAzkiKEb1I=s1360-w1360-h1020", "lake"),
]

class BreedsList(TemplateView):
    template_name = "breeds_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["breeds"] = breeds
        return context


class Activity:
    def __init__(self, name, image, description):
        self.name = name
        self.image = image
        self.description = description


activitieslevel = [
  Activity ("Low", "",
          "Blah"),
  Activity ("High",
          "", "info"),
]

class ActivityLevelList(TemplateView):
    template_name = "activitieslevel_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activitieslevel"] = activitieslevel
        return context
