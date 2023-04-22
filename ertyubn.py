import sqlite3

import requests

from bs4 import BeautifulSoup

from datetime import datetime

conn = sqlite3.connect('weather')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS weather(date DATE,time TIME,temperature REAL)''')

url = 'https://meteopost.com/city/28368/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

temperature = float(soup.find('span', class_='t').text)


now = datetime.now()

date = now.strftime('%Y-%m-%d')

time = now.strftime('%H:%M:%S')

c.execute('INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)', (date, time, temperature))

conn.commit()

conn.close()




















#id INTEGER PRIMARY KEY AUTOINCREMENT,

