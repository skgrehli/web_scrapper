from django.shortcuts import render
from django.http import HttpResponse
from .models import Scraper_data
# Create your views here.

def index(request):
	# import pdb;pdb.set_trace()
	if request.method == "POST":
		urls = request.POST.get('urls')
		insert = Scraper_data.objects.create(urls=urls)
		insert.save() 
		return render(request, "index.html" ,{'msg':"data succesfully saved"})
	return render(request, "index.html")

def show_data(request):
	# import pdb;pdb.set_trace()
	# if request.method == "POST":
	# 	urls = request.POST.get('urls')
	# 	insert = Scraper_data.objects.create(urls=urls)
	# 	insert.save() 

	# 	return render(request, "show_detail.html")
	return render(request, "show_detail.html")




	# u_id = Scraper_data.objects.filter(urls=urls)
	# 	for i in u_id:
	# 		id = i.id
	# 	# data_id = Scraper_data.objects.filter(id=id)
	# 	print (data_id)