import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.morizon.pl/mieszkania/warszawa/praga-poludnie/?ps%5Bowner%5D%5B0%5D=4'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', class_='property_link property-url')

with open('morizon_links.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for link in links:
        writer.writerow([link['href']])



response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', class_='property_link property-url')

with open('morizon_links.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for link in links:
        writer.writerow([link['href']])