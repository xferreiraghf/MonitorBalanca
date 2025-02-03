from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    company = models.CharField(max_length=100)           
    operating_system = models.CharField(max_length=50) 
    ip_address = models.GenericIPAddressField(null=True, blank=True) 
    flask_port = models.IntegerField(default=5000)  

    def __str__(self):
        return f"{self.name} - {self.company}"
