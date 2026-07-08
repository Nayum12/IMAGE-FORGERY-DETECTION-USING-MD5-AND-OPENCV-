from django.db import models
import os

# Create your models here.


class UserModel(models.Model):
    """Stores registered user information and profile picture."""
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    contact = models.IntegerField()
    address = models.CharField(max_length=100)
    # Profile pictures are saved to media/profiles/
    profile = models.FileField(upload_to='profiles/')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "UserModel"


class Images(models.Model):
    """Stores pairs of uploaded images and their forgery detection result."""
    # Images are saved to media/uploads/
    image1 = models.FileField(upload_to='uploads/')
    image2 = models.FileField(upload_to='uploads/')
    output = models.CharField(max_length=100, null=True)
    uploader = models.EmailField(null=True)

    def filename1(self):
        return os.path.basename(self.image1.name)

    def filename2(self):
        return os.path.basename(self.image2.name)

    class Meta:
        db_table = 'Images'