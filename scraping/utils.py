import os
import re
import sys
import time
import json
from random import randint
from pyvirtualdisplay import Display
from selenium import webdriver
import csv

from django.conf import settings
from scraping.models import ScraperData


def scrape_website_data(domain, fetch_url, id):
    browser = None
    display = Display(visible=0, size=(800, 600))
    display.start()
    try:
        browser = webdriver.Chrome()
    except Exception as error:
        print(error)

    if browser is None:
        print("Selenium not opened")
        return
    filename = "%s_data_file_%s.csv" % (domain, str(id))
    file_path = os.path.join(settings.BASE_DIR, 'output', filename)
    with open(file_path, "w") as out_file:
        writer = csv.writer(out_file)
        offset = 1
        flag = True
        writer.writerow(['Business Name', 'Phone', 'Address',
                         'Category Type', 'Website'])

        while flag:
            url = fetch_url + '&page=%s' % (offset)
            browser.get(url)
            time.sleep(10)
            offset += 1
            url_link = False
            for element in browser.find_elements_by_css_selector('div.search-results div.result div.info'):
                url_link = True
                try:
                    business_name = element.find_element_by_css_selector(
                        'a.business-name span').text.strip().encode('ascii', 'ignore').decode('ascii')
                except Exception as e:
                    business_name = ''
                try:
                    phone = element.find_element_by_css_selector(
                        'div.phone.primary').text.strip().encode('ascii', 'ignore').decode('ascii')
                except Exception as e:
                    phone = ''
                try:
                    street_address = element.find_element_by_css_selector(
                        'div.street-address').text.strip().encode('ascii', 'ignore').decode('ascii')
                    locality = element.find_element_by_css_selector(
                        'div.locality').text.strip().encode('ascii', 'ignore').decode('ascii')
                    address = street_address + ', ' + locality
                except Exception as e:
                    address = ''
                try:
                    category_type = element.find_element_by_css_selector(
                        'div.categories').text.strip().encode('ascii', 'ignore').decode('ascii')
                except Exception as e:
                    category_type = ''
                try:
                    website = element.find_element_by_css_selector(
                        'div.links a.track-visit-website').get_attribute('href').strip().encode('ascii', 'ignore').decode('ascii')
                except Exception as e:
                    website = ''

                try:
                    writer.writerow(
                        [business_name, phone, address, category_type, website])
                except Exception as e:
                    print(e)
            if not url_link:
                flag = False
    browser.quit()
    scraper_data  = ScraperData.objects.get(pk=id)
    scraper_data.is_processing = False
    scraper_data.save()
    display.stop()

