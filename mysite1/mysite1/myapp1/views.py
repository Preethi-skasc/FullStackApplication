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
            return JsonResponse({"message:","invalid Email or Password"})
    return JsonResponse({"Error":"Post Method Only"})
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        email = data.get("email")
        password = data.get("password")

        user = Register.objects.filter(Email=email, Password=password).first()

        if user:
            return JsonResponse({
                "message": "Login Successful",
                "user": {
                    "id": user.id,
                    "Firstname": user.Fname,
                    "Lastname": user.Lname,
                    "Phone": user.Phone,
                    "Email": user.Email
                }
            })
        else:
            return JsonResponse({"message": "Invalid Email or Password"}, status=401)

    return JsonResponse({"Error": "POST method only"})

