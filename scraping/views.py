from django.shortcuts import render
from django.http import HttpResponse
from scraping.models import ScraperData


def index(request):
    
    if request.method == "POST":

        url = request.POST.get('url')
      
        domain=url.split("//")[-1].split("/")[0]
        
        insert = ScraperData.objects.create(url=url, domain= domain)
        insert.save()
        return render(request, "index.html", {'msg': "data succesfully saved"})
    return render(request, "index.html")


def show_data(request):

    url_data = ScraperData.objects.all()
    return render(request, "show_detail.html",{'data':url_data})


# domain url status