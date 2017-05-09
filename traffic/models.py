from django.db import models

# Create your models here.
##  class holding information about client
class Client(models.Model):
    clientIP = models.GenericIPAddressField(unique=True)
    clientName = models.CharField(max_length=50)
    clientcomment = models.CharField(max_length=300)

    def __str__(self):
        return self.clientIP
#Class holding download upload data for particular month
class Traffic(models.Model):
    trafficDownload = models.FloatField()
    trafficUpload = models.FloatField()
    trafficIP = models.ForeignKey(Client,related_name="traffic_for_client", unique_for_date="trafficTime")
    trafficTime = models.DateField()

    def __str__(self):
        return '%s %s' % (self.trafficIP, self.trafficTime)