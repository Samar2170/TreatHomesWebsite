from django.shortcuts import render,redirect
from .models import Sites, FrontImages, Services,AncilServices,USP, FAQ,PhoneLead, ServiceFeatures
from django.views import View
from .models import Lead
from .forms import LeadForm

#add query form
def home(request):
    imgs=FrontImages.objects.all()
    sites=Sites.objects.all()[:4]
    ancl_services=AncilServices.objects.all()
    usp=USP.objects.all()
    services=Services.objects.all()
    return render(request, "home.html",{"imgs":imgs, "sites":sites, "ancs":ancl_services, "usp":usp, "services":services})


def sites(request):
    sites=Sites.objects.all()
    return render(request,"sites.html", {"sites":sites})


#query form for each 
def site(request,site_id):
    sites=Sites.objects.all()[:4]
    site=Sites.objects.get(id=site_id)
    ancl_services=AncilServices.objects.all()
    sites=Sites.objects.all()[:3]
    return render(request,"site.html", {"site":site,"ancs":ancl_services, "sites":sites})

class Contact(View):
    def get(self,request):
        form=LeadForm()
        return render(request, "form.html",{"form":form})
    def post(self,request):
        form=LeadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)    
        
def about(request):
    return render(request, "about.html")    

def faq(request):
    faq=FAQ.objects.all()
    sites=Sites.objects.all()[:4]
    faq1=[f for f in faq if (f.id%2)==0]
    faq2=[f for f in faq if (f.id%2)!=0]
    return render(request,"faq.html",{"faq1":faq1,"faq2":faq2,"sites":sites})

def service(request,service_id):
    sites=Sites.objects.all()[:4]
    service=Services.objects.get(id=service_id)
    service_fts=ServiceFeatures.objects.filter(service_id=service_id)
    return render(request,'service.html',{"service":service, "service_fts":service_fts,"sites":sites})

def subscribe(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        P=PhoneLead(phone=phone)
        P.save()
        return redirect(home)
    else:
        return HttpResponse('this is post requests')
def test(request):
    return render(request, "test_alpine.html")