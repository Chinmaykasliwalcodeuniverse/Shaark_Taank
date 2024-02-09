from django.shortcuts import render
from .models import entrepreneur
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
  entrepreneurs=entrepreneur.objects.all()
  query=""
  if request.method =='POST':
    if "add" in request.POST:
      name= request.POST.get("name")
      email=request.POST.get("email")
      entrepreneur.objects.create(
        name=name,
        email=email
      )
      messages.success(request,"Entrepreneur Successfully Added")
    elif "update" in request.POST:
      id = request.POST.get("id")
      name=request.POST.get("name")
      email=request.POST.get("email")

      update_entrepreneur= entrepreneur.objects.get(id=id)
      update_entrepreneur.name=name
      update_entrepreneur.email=email
      update_entrepreneur.save()
      messages.success(request,"successfully updated")
    elif "delete" in request.POST:
      id =request.POST.get("id")
      entrepreneur.objects.get(id=id).delete()
      messages.success(request,"Entrepreneur Successfully Deleted")
    elif "search" in request.POST:
      query=request.POST.get("searchquery")
      entrepreneurs=entrepreneur.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
  context={"entrepreneurs":entrepreneurs,"query":query}
  return render(request,"index.html",context=context)


def home(request):
  return render(request,"master.html")
