from django.shortcuts import render
from django.views import View 
from .models import Breed
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"



#### Breed List #########
# class Breed:
#     def __init__(self, name, img, description):
#         self.name = name
#         self.img = img
#         self.description = description


breeds = [
  Breed ("Little Spokane River", "https://assets.change.org/photos/9/lq/sr/HuLQsrEXlyAdApc-1600x900-noPad.jpg?1622402845",
          "Blah"),
  Breed ("Heyburn State Park",
          "https://lh3.googleusercontent.com/p/AF1QipOheBfE-Bixtqcbm3zw5N_wif3JiDaAzkiKEb1I=s1360-w1360-h1020", "lake"),
]

class BreedList(TemplateView):
    template_name = "breed_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["breeds"] = Breed.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["breeds"] = Breed.objects.all()
            # default header for not searching 
            context["header"] = "Trending Breeds"
        return context

class BreedDetail(DetailView):
    model = Breed
    template_name = "breed_detail.html"
    
class BreedCreate(CreateView):
    model = Breed
    fields = ['name', 'img', 'description']
    template_name = "breed_create.html"
    # this will get the pk from the route and redirect to artist view
    def get_success_url(self):
        return reverse('breed_detail', kwargs={'pk': self.object.pk})
        
        
class BreedUpdate(UpdateView):
    model = Breed
    fields = ['name', 'img', 'description']
    template_name = "breed_update.html"

    def get_success_url(self):
        return reverse('breed_detail', kwargs={'pk': self.object.pk})  
    
    
    
# class Activity:
#     def __init__(self, name, image, description):
#         self.name = name
#         self.image = image
#         self.description = description


# activitieslevel = [
#   Activity ("Low", "",
#           "Blah"),
#   Activity ("High",
#           "", "info"),
# ]

# class ActivityLevelList(TemplateView):
#     template_name = "activitieslevel_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["activitieslevel"] = activitieslevel
#         return context
