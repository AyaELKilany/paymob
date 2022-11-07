from django.db import models

# Create your models here.


from django.db import models

# Create your models here.
class Payment(models.Model):
    client_name = models.CharField(max_length=30)
    value = models.IntegerField()
    currency = models.CharField(max_length=20)
    
    def __str__(self):
        return self.client_name