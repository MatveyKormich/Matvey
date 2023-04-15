from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup
import time, requests, lxml

def run(playwright):
    page = playwright.chromium.launch(headless=False).new_page()
    page.goto('https://www.booking.com/searchresults.ru.html?ss=%D0%94%D0%BD%D0%B5%D0%BF%D1%80%2C+%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D0%B0&efdco=1&label=slh1_-KHnYBqoTN21xDbVSl4NA3QS502774686649%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-334108349%3Alp1030260%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YTQUGSsRwx9_piJbnTYecvA&aid=376445&lang=ru&sb=1&src_elem=sb&src=index&dest_id=-1037865&dest_type=city&checkin=2023-04-21&checkout=2023-04-22&group_adults=2&no_rooms=1&group_children=1&age=9&sb_travel_purpose=leisure')
    time.sleep(2)
    soup = BeautifulSoup(page.content(), 'lxml')

    for hotel in soup.select('.a4225678b2'):
        title = hotel.select_one('[data-testid="title"]').text
        link = hotel.select_one('a').get('href')
        print(title, link)

with sync_playwright() as playwright:
    run(playwright)

