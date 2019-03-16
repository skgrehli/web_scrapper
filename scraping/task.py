import logging
from django.urls import reverse
from scraping.utils import scrape_website_data
from scraping.models import ScraperData
from Scraping.celery import app

@app.task
def run_scraping(domain ,fetch_url, id):
    scrape_website_data(domain ,fetch_url, id)