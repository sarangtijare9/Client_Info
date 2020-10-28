from django.shortcuts import render
from django.http import HttpResponse
from .models import Client
from .models import Media_File


# Create your views here.
def index(request):



    if request.method == "POST":

        bname = request.POST.get('bname', '')

        name = request.POST.get('name', '')

        phone = request.POST.get('phone', '')

        email = request.POST.get('email', '')

        address = request.POST.get('address', '')

        r = Client(Bussiness_name=bname,Full_name=name, Email=email, Phone=phone,Address=address)
        r.save()

        print(bname,name,phone, email, address)



    return render(request, "app/index2.html")


def nextpage(request):


    if request.method == "POST":

        domain = request.POST.get('domain', '')

        logos = request.FILES.get('logos', '')

        image = request.FILES.get('image', '')

        headline = request.POST.get('headline', '')


        s=Media_File(Domain=domain,Logos=logos,Image=image,Headline=headline)
        s.save()

        print(domain,logos,image,headline )




    return render(request, "app/index3.html")