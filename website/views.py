from django.shortcuts import render
from .models import contact
from .models import servicesmodel, pricemodel



def home(request):
    if request.method=='POST':
    #   email= request.POST['email']
    #   password= request.POST['password']
      name= request.POST['name']
      address= request.POST['address']
      city= request.POST['city']
      state= request.POST['state']
      print(name, address, city, state)
      obj= contact( name= name ,address= address, city=city, state=state)
      obj.save()
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    serv = servicesmodel.objects.all()
    print(serv)
    return render(request, 'services.html', {'serv': serv})

def prices(request):
      prc= pricemodel.objects.all()
      print(prc)
      return render(request, 'prices.html',  {'prc': prc})

def contactlist(request):
    if request.method=='POST':
    #   email= request.POST['email']
    #   password= request.POST['password']
      name= request.POST['name']
      address= request.POST['address']
      city= request.POST['city']
      state= request.POST['state']
      print(name, address, city, state)
      obj= contact( name= name ,address= address, city=city, state=state)
      obj.save()
    return render(request, 'contact.html')
def test(request):
    return render(request, 'test.html')
def kkk(request):
    return render(request, 'test.html')