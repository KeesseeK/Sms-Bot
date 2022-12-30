import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.morizon.pl/mieszkania/warszawa/goclaw/?ps%5Bprice_from%5D=370000&ps%5Bprice_to%5D=600000&ps%5Bowner%5D%5B0%5D=4'
links = []
numbers = []

def get_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    soup_links = soup.find_all('a', class_='property_link property-url')
  
    with open('morizon_links.csv', 'w') as morizon_links:
      writer = csv.writer(morizon_links)
      for soup_link in soup_links:
          writer.writerow([soup_link['href']])
          links.append(soup_link['href'])

def get_numbers(links):
    for link in links:
      url2 = link
      urls_response = requests.get(url2)
      soup = BeautifulSoup(urls_response.text, 'html.parser')
      soup_links = soup.find_all('span', class_='phone hidden')
      numbers.append(soup_links[0].text)

      with open('numbers.csv', 'w') as numberscsv:
        writer = csv.writer(numberscsv)
        for number in numbers:
            writer.writerow([number])
          
def writing_to_csv(numbers, links):
    with open('data.csv', 'w') as d:
      writer = csv.writer(d)
      writer.writerows(zip(numbers,links))


get_links(url)
get_numbers(links)
writing_to_csv(numbers, links)
