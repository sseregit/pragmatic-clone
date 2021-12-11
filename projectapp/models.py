from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='project/', null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title