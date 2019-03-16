from django.shortcuts import render
from django.http import HttpResponse
from scraping.models import ScraperData


def index(request):
    if request.method == "POST":
        urls = request.POST.get('urls')
        insert = ScraperData.objects.create(urls=urls)
        insert.save()
        return render(request, "index.html", {'msg': "data succesfully saved"})
    return render(request, "index.html")


def show_data(request):

    return render(request, "show_detail.html")
