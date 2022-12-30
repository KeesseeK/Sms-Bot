import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.morizon.pl/mieszkania/warszawa/praga-poludnie/?ps%5Bowner%5D%5B0%5D=4'
urls_response = requests.get(url)
soup = BeautifulSoup(urls_response.text, 'html.parser')
soup_links = soup.find_all('a', class_='property_link property-url')
links = []

with open('morizon_links.csv', 'w') as morizon_links:
    writer = csv.writer(morizon_links)
    for soup_link in soup_links:
        writer.writerow([soup_link['href']])
        links.append(soup_link['href'])



numbers_response = requests.get(links[0])
print(numbers_response.text)
soup2 = BeautifulSoup(numbers_response.text, 'html.parser')
numbers = soup2.find_all('span ', class_='phone hidden')

with open('morizon_numbers.csv', 'w') as morizon_numbers:
    writer = csv.writer(morizon_numbers)
    for number in numbers:
        writer.writerow([number])
