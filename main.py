import requests
from bs4 import BeautifulSoup
import csv

urls = ['https://www.morizon.pl/mieszkania/warszawa/goclaw/?ps%5Bprice_from%5D=370000&ps%5Bprice_to%5D=600000&ps%5Bowner%5D%5B0%5D=4']



class Scrape:
  def get_links(self, urls):
    for url in urls:
        url_response = requests.get(url)
        soup = BeautifulSoup(url_response.text, 'html.parser')
        soup_links = soup.find_all('a', class_='property_link property-url')
        links = []
        for soup_link in soup_links:
            links.append(soup_link['href'])
    print(links)
    return links
  
  
  def get_numbers(self, links):
    numbers = []
    for link in links:
      number_response = requests.get(link)
      soup = BeautifulSoup(number_response.text, 'html.parser')
      soup_number= soup.find_all('span', class_='phone hidden')
      numbers.append(soup_number[0].text)
    print(numbers)
    return numbers

class Data:
  def write_to_csv(self, links, numbers):
    try:
      with open("data.csv", 'w') as csvfile:
        headers = ["Number","Link"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerow(links)
        writer.writerow(numbers)
    except IOError:
      print("I/O error")


if __name__ == '__main__':
  scrape = Scrape()
  data = Data()
  data.write_to_csv(scrape.get_numbers(scrape.get_links(urls)))