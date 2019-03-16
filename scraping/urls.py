from django.conf.urls import url
from . import views

app_name="scraping"

urlpatterns = [

    url(r'download/(?P<id>\d)/', views.file_download, name='download'),
    url('show_data/', views.show_data, name='show_data'),
    url('', views.index, name='home'),
    
    ]
