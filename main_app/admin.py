from django.contrib import admin
from .models import Breed, Activity, DogOwnerWants

admin.site.register(Breed)
admin.site.register(Activity)
admin.site.register(DogOwnerWants)
