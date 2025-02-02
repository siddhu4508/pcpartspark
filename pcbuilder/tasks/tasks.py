# task.py (Celery task)

from celery import shared_task
import requests
from bs4 import BeautifulSoup


@shared_task
def scrape_filpkart_prices(request):
    url = 'https://www.flipkart.com/search?q=graphic+card'
    response = requests.get(url, headers={'User-Agent': "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='_1AtVbE')
    prices = []
    
    for product in products:
        title = product.find('a', class_='IRpwTa').text
        price = product.find('div', class_='_30jeq3').text
        prices.append((title, price))
    return prices


