from .models import Person, Vehicle
from django.shortcuts import redirect, render
from .forms import PersonForm, VehicleForm, VehicleEditForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.
def person(request, template_name="person.html"):
    p = Person.objects.all()
    context = {
        'persons': p
    }
    return render(request, template_name, context)

def create_person(request, template_name="create_person.html"):
    context ={}
 
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("person")
         
    context['form']= form
    return render(request, template_name, context)

def update_person(request, id, template_name = "update_person.html"):
    context = {}
    obj = get_object_or_404(Person, id = id)
    form = PersonForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return redirect("person")

    context["form"] = form
 
    return render(request, template_name, context)

def delete_person(request, id):
    obj = get_object_or_404(Person, id = id)
 
    if request.method =="POST":
        obj.delete()
       
    return redirect("person")


def vehicle(request, template_name="vehicle.html"):
    v = Vehicle.objects.all()
    context = {
        'vehicles': v
    }
    return render(request, template_name, context)

def create_vehicle(request, template_name="create_vehicle.html"):
    context ={}
 
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        owner_id = form.data['owner']
        owner = get_object_or_404(Person, id = owner_id)
        
        vehicles_owner = Vehicle.objects.filter(owner__id = owner_id)
        if len(vehicles_owner) < 3:
            owner.sale_opportunity = False
            owner.save()
            form.save()
            return redirect("vehicle")
        else:
            context['alert'] = 'Registration not allowed, only 3 vehicles per person.'    
            
    context['form']= form
    return render(request, template_name, context)

def update_vehicle(request, id, template_name = "update_vehicle.html"):
    context = {}
    obj = get_object_or_404(Vehicle, id = id)
    form = VehicleEditForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return redirect("vehicle")

    context["form"] = form
 
    return render(request, template_name, context)

def delete_vehicle(request, id):
    obj = get_object_or_404(Vehicle, id = id)
 
    if request.method =="POST":
        owner_id = obj.owner.pk
        vehicles_owner = Vehicle.objects.filter(owner__id = owner_id)
        if len(vehicles_owner) == 1:
            owner = get_object_or_404(Person, id = owner_id)
            owner.sale_opportunity = True
            owner.save()
        
        obj.delete()
       
    return redirect("vehicle")