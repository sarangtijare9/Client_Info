from django.db import models


class Client(models.Model):
    Bussiness_name =models.CharField(max_length=50)
    Full_name = models.CharField(max_length=50)
    Phone =models.CharField(max_length=30)
    Email = models.EmailField()
    Address =models.CharField(max_length=100)


    def __str__(self):

        return self.Full_name



class Media_File(models.Model):

    Domain =models.CharField(max_length=50,default="")
    Logos=models.FileField(null=True)
    Image=models.FileField(null=True)
    Headline=models.CharField(max_length=100,default="")



    def __str__(self):

        return self.Domain


