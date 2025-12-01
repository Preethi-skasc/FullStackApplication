from django.shortcuts import render

# Create your views here.
import json
from .models import Register
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def reg(request):
    if request.method =="POST":
        data=json.loads(request.body.decode("utf-8"))
        Fname = data.get("Fname")
        Lname = data.get("Lname")
        Phone = data.get("Phone")
        Email = data.get("Email")
        Password = data.get("Password")

        Register.objects.create(
            Fname = Fname,
            Lname = Lname,
            Phone = Phone,
            Email = Email,
            Password = Password


        )

        return JsonResponse({"message":"Registered successfully"},status = 201)
    return JsonResponse({"Error":"Post Method Only"},status = 405)
@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        Email = data.get("Email")
        Password = data.get("Password")

        user = Register.objects.filter(Email=Email,Password=Password)
        if user:
            return JsonResponse({"message":"Login Successfully"})
        else:
            return JsonResponse({"message:":"invalid Email or Password"})
    return JsonResponse({"Error":"Post Method Only"})

@csrf_exempt 
def get_data(request):
   if request.method =="GET":
     data = Register.objects.all()
     sample = []
   for users in data :
        sample.append({
           "Firstname":users.Fname,
           "Lastname":users.Lname,
           "Phone":users.Phone,
           "Email":users.Email,
           "Password":users.Password
        })

        return JsonResponse({"Details":sample})
   return JsonResponse({"Error":"Get Method only"})


@csrf_exempt
def delete_data (request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")
        remove = Register .objects.filter(id=Id)
        if remove.exists():
            remove.delete()
            return JsonResponse({"message":"Deleted sccesfully"})
        else:
            return JsonResponse({"message":"Deleted unsuccessfully"})
    return JsonResponse({"Error":"Delete meethos only"})


@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")
        if not Register.objects.filter(id=Id).exists():
            return JsonResponse({"message":"User not found"})
        Register.objects.filter(id=Id).update(
        Fname = data.get("Fname"),
        Lname = data.get("Lname"),
        Phone = data.get("Phone"),
        Email = data.get("Email"),
        Password = data.get("Password")
        )
        return JsonResponse({"message":"updated successfully"})
    return JsonResponse({"error":"PUT method only"})