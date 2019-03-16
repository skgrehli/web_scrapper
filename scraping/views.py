import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from scraping.models import ScraperData
from .task import run_scraping

def index(request):
    
    if request.method == "POST":

        url = request.POST.get('url')
      
        domain=url.split("//")[-1].split("/")[0]
        
        insert = ScraperData.objects.create(url=url, domain= domain)
        insert.save()
        run_scraping.delay(insert.domain, insert.url, insert.id)        
        return render(request, "index.html", {'msg': "Data Scrapping request added Sucessfully."})
    return render(request, "index.html")


def show_data(request):

    url_data = ScraperData.objects.all()
    return render(request, "show_detail.html",{'data':url_data})


# domain url status

def file_download(request, id):
    scraper_data = ScraperData.objects.get(id=id) 
    filename = "%s_data_file_%s.csv" % (scraper_data.domain, str(id))
    file_path = os.path.join(settings.BASE_DIR, 'output', filename)
    with open(file_path, "rb") as pdf:
        response = HttpResponse(pdf.read())
        response['content_type'] = 'application/pdf'
        response['Content-Disposition'] = 'attachment;filename=%s' % filename
        return response
    return None

    


 
