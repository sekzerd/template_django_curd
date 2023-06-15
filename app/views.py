from django.shortcuts import render
from django import http
from app.models import User


def index(request):
    return render(request, "index.html")


def create(request):
    return render(request, "create.html")


def retrieve(request):
    data = User.objects.all()
    context = {"data": data}
    return render(request, "retrieve.html", context)


def update(request, id):
    user = User.objects.get(id=id)
    context = {"user": user}
    return render(request, "update.html", context)


def delete(request):
    return render(request, "delete.html")


def do_update(request):
    user = User.objects.get(id=request.POST["id"])
    user.id = request.POST["id"]
    user.name = request.POST["name"]
    user.age = request.POST["age"]
    user.address = request.POST["address"]
    user.save()
    # return redirect(to="list")
    return http.HttpResponse("do_update ok")


def do_delete(request):
    user = User.objects.get(id=request.POST["id"])
    user.delete()
    # return redirect(to="list")
    return http.HttpResponse("do_delete ok")


def do_create(request):
    user = User()
    user.id = request.POST["id"]
    user.name = request.POST["name"]
    user.age = request.POST["age"]
    user.address = request.POST["address"]
    user.save()
    return http.HttpResponse("do_create ok")
