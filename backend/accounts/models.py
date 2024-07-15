from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mission(models.Model):
    libelle = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return f"{self.libelle}"
    
class UserMission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + self.mission.libelle