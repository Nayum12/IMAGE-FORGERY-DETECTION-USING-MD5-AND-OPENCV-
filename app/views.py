from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from .detect import *


# Create your views here.
def index(request):
    return render(request, 'index.html')            

def about(request):
    return render(request, 'about.html')

def userslogin(request):
    if request.method == 'POST':
        email =request.POST['email']
        password = request.POST['password']
        data = UserModel.objects.filter(email=email, password=password).exists()

        if data:
            request.session['email']=email
            return redirect('home')
        else:
            messages.success(request, 'Invalid Credentails!')
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
            messages.success(request, 'Email already existed')
            return redirect('userregister')
        else:
            UserModel.objects.create(name=name, email=email, password=password, dob=dob, gender=
                                      gender, contact=contact, address=address, profile=profile).save()
            messages.success(request, 'Registration Successfull')
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

        image = Images(image1 = img1, image2 = img2, uploader = email)
        image.save()

        fimg1 = image.image1.name
        fimg2 = image.image2.name

        print(fimg1)
        print(fimg2)
        result = ""
        if (similar(fimg1, fimg2)):
            if (createHash(fimg1,fimg2)):
                result = "Image is Same."
            else:
                result = "Image is Different"
        else:
            result = "Image is Different"
        data = Images.objects.get(id=image.id)
        data.output = result
        data.save()
        print(result)
        messages.success(request, f'Output :{result}')

    return render(request,"uploadfile.html")



# import os
# import hashlib


# def compute_sha256(file_path):
#     """
#     Compute SHA-256 hash of a file.
#     """
#     with open(file_path, "rb") as img_file:
#         img_bytes = img_file.read()
#         return hashlib.sha256(img_bytes).hexdigest()

# def uploadfile(request):
#     if request.method == 'POST':
#         email = request.session.get('email', None)

#         img1 = request.FILES["upload1"]
#         img2 = request.FILES["upload2"]

#         # Save uploaded images
#         image = Images(image1=img1, image2=img2, uploader=email)
#         image.save()

#         # Get full file paths
#         file1_path = image.image1.path
#         file2_path = image.image2.path

#         # Compute SHA-256 hashes
#         hash1 = compute_sha256(file1_path)
#         hash2 = compute_sha256(file2_path)

#         # print(f"Image 1 SHA-256: {hash1}")
#         # print(f"Image 2 SHA-256: {hash2}")

#         if (similar(file1_path, file2_path)):

#             if hash1 == hash2:
#                 result = "Image is Same."
#             else:
#                 result = "Image is Different"
#         else:
#             result = "Image is Different"

#         # Save result to DB
#         image.output = result
#         image.save()

#         messages.success(request, f'Output :{result}')

#     return render(request,"uploadfile.html")



def viewdata(request):
    email = request.session['email']
    images = Images.objects.filter(uploader=email)
    # print(type(images))
    return render(request, 'viewdata.html', {'data': images})
