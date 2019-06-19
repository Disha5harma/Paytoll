from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import car_detail


def Car_no(request):
        Car_no = request.GET.get('car_number')
        return render(request,'home.html')

def Tax(request):
        Car_no = request.GET.get('car_number')
        flag=0
        print()
        cd={}
        cd=car_detail.objects.all()
        for cn in cd:
                if(Car_no==cn.car_number):
                        if(cn.diesel_fuel==1):
                                fn="DIESEL"
                                tax= "20%"+ "extra"
                        else:
                                fn="PETROL"
                                tax = "20%" + "less" 
                        flag=1
                
        if (flag==0):
                fn="NOT FOUND"
                tax ="NOT FOUND" 
                 
        return render(request,'tax.html',{'fu':fn,'t':tax})

def about(request):
        return render(request,'about.html')

def contact(request):
        return render(request,'contact.html')

def learnmore(request):
        return render(request,'use.html')

