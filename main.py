import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.morizon.pl/mieszkania/warszawa/praga-poludnie/?ps%5Bowner%5D%5B0%5D=4'
links = []
numbers = []

def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        if link.get('href'):
            links.append(link.get('href'))

def get_numbers(links):
    for link in links:
      r = requests.get(link)
      soup = BeautifulSoup(r.text, 'html.parser')
      for link in soup.find_all('span', class_='number')

                              

urls_response = requests.get(url)
soup = BeautifulSoup(urls_response.text, 'html.parser')
soup_links = soup.find_all('a', class_='property_link property-url')
links = []
numbers = []

with open('morizon_links.csv', 'w') as morizon_links:
    writer = csv.writer(morizon_links)
    for soup_link in soup_links:
        writer.writerow([soup_link['href']])
        links.append(soup_link['href'])

for link in links:
  url2 = link
  urls_response = requests.get(url2)
  soup = BeautifulSoup(urls_response.text, 'html.parser')
  soup_links = soup.find_all('span', class_='phone hidden')
  numbers.append(soup_links[0].text)

with open('morizon_links2.csv', 'w') as morizon_links2:
    writer = csv.writer(morizon_links2)
    for number in numbers:
        writer.writerow([number])

print(numbers)