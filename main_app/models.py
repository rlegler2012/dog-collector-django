from django.db import models

class Breed(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        
class Activity(models.Model):

    level = models.CharField(max_length=150)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="activitys")

    def __str__(self):
        return self.level

class DogOwnerWants(models.Model):
    level = models.CharField(max_length=150)
    activitys = models.ManyToManyField(Activity)

    def __str__(self):
        return self.level

