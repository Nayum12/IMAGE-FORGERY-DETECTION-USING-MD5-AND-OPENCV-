from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from . models import *
from .detect import *
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def userslogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        data = UserModel.objects.filter(email=email, password=password).exists()

        if data:
            request.session['email'] = email
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentials!')
            return redirect('userslogin')
    return render(request, 'userslogin.html')


def userregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']
        contact = request.POST['contact']
        address = request.POST['address']
        profile = request.FILES['profile']

        if UserModel.objects.filter(email=email).exists():
            messages.success(request, 'Email already exists')
            return redirect('userregister')
        else:
            UserModel.objects.create(
                name=name, email=email, password=password,
                dob=dob, gender=gender, contact=contact,
                address=address, profile=profile
            ).save()
            messages.success(request, 'Registration Successful')
            return redirect('userslogin')

    return render(request, 'userregister.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    del request.session['email']
    return redirect('index')


def uploadfile(request):
    email = request.session['email']
    if request.method == 'POST':
        img1 = request.FILES["upload1"]
        img2 = request.FILES["upload2"]

        # Save the uploaded images to the database (stored in media/uploads/)
        image = Images(image1=img1, image2=img2, uploader=email)
        image.save()

        # Build full absolute paths so OpenCV and md5hash can read the files
        fimg1 = os.path.join(settings.MEDIA_ROOT, image.image1.name)
        fimg2 = os.path.join(settings.MEDIA_ROOT, image.image2.name)

        print("Image 1 path:", fimg1)
        print("Image 2 path:", fimg2)

        result = ""
        if similar(fimg1, fimg2):
            if createHash(fimg1, fimg2):
                result = "Image is Same."
            else:
                result = "Image is Different"
        else:
            result = "Image is Different"

        # Save result to database
        data = Images.objects.get(id=image.id)
        data.output = result
        data.save()

        print("Detection result:", result)
        messages.success(request, f'Output: {result}')

    return render(request, "uploadfile.html")


def viewdata(request):
    email = request.session['email']
    images = Images.objects.filter(uploader=email)
    return render(request, 'viewdata.html', {'data': images})
