from django.db import models

class Skill(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False, null=False)
    
    def __str__(self):
        return self.title
    

