from typing import Any, Dict
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View 
from .models import Breed, Activity, DogOwnerWants
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wants"] = DogOwnerWants.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"



#### Breed List #########
breeds = [
  Breed ("Golden Retriver", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKeOgOtWPQr7lRf43oA4tt-5fM1jS2-pn7_A&usqp=CAU",
          "sdfwerweerqerrtr"),
  Breed ("Pitbull",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRobw8jCAd-h8AzTFxXZtmI6HO_25StC3rHGg&usqp=CAU", "lweqererqewrqwerwerw"),
]

class BreedList(TemplateView):
    template_name = "breed_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["breeds"] = Breed.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            # context["header"] = f"Searching for {name}"
        else:
            context["breeds"] = Breed.objects.all()
            # default header for not searching 
            # context["header"] = "Trending Breeds"
        return context

class BreedDetail(DetailView):
    model = Breed
    template_name = "breed_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wants"] = DogOwnerWants.objects.all()
        return context
    
class BreedCreate(CreateView):
    model = Breed
    fields = ['name', 'img', 'description']
    template_name = "breed_create.html"
    success_url = '/breeds/'  
             
class BreedUpdate(UpdateView):
    model = Breed
    fields = ['name', 'img', 'description']
    template_name = "breed_update.html"
    success_url = '/breeds/'
    # def get_success_url(self):
    #     return reverse('breed_detail', kwargs={'pk': self.object.pk})  
    
class BreedDelete(DeleteView):
    model = Breed
    template_name = "breed_delete_confirmation.html"
    success_url = "/breeds/"   
    

#### Activity List #########
activitys = [
  Activity ("Low"),
  Activity ("Low to Medium"),
  Activity ("Medium"),
  Activity ("High"),
]

class ActivityList(TemplateView):
    template_name = "activity_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activitys"] = Activity.objects.all()
        return context
    
class ActivityCreate(View):

    def post(self, request, pk):
        level = request.POST.get("level")
        breed = Breed.objects.get(pk=pk)
        Activity.objects.create(level=level, breed=breed)
        return redirect('breed_detail', pk=pk)

# class Activity:
#     def __init__(self, level):
#         self.level = level

class DogOwnerWantsAssoc(View):

    def get(self, request, pk, activity_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            DogOwnerWants.objects.get(pk=pk).activitys.remove(activity_pk)
        if assoc == "add":
            DogOwnerWants.objects.get(pk=pk).activitys.add(activity_pk)
        return redirect('home')