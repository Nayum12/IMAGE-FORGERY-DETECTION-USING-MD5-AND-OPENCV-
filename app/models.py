from django.db import models
import os
# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    profile = models.FileField(upload_to=os.path.join('static', 'UserModel'))
    

    def __str__(self):  
        return self.name
    
    class Meta:
        db_table = "UserModel"


from django.db import models
import os

# Create your models here.
class Images(models.Model):
    image1 = models.FileField(upload_to="static/uploads")
    image2 = models.FileField(upload_to="static/uploads")
    output = models.CharField(max_length=100,null=True)
    uploader = models.EmailField(null=True)


    def filename1(self):
        return os.path.basename(self.image1.name)

    def filename2(self):
        return os.path.basename(self.image2.name)
    
        
    class Meta:
        db_table = 'Images'