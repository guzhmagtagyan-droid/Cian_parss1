import requests
from bs4 import BeautifulSoup

class CianParser:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_listing_page(self, page_number=1):
        response = requests.get(f'{self.base_url}?page={page_number}')
        response.raise_for_status()  # Raise an error for bad responses
        return response.text

    def parse_listing(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        listings = []
        for item in soup.find_all('div', class_='c5wKvs'):
            title = item.find('h3').text.strip()  # Extract the title
            image_url = item.find('img')['src']  # Extract the image URL
            listings.append({'title': title, 'image_url': image_url})
        return listings

    def get_all_listings(self, total_pages):
        all_listings = []
        for page in range(1, total_pages + 1):
            html = self.get_listing_page(page)
            listings = self.parse_listing(html)
            all_listings.extend(listings)
        return all_listings

# Example usage:
# parser = CianParser('https://www.cian.ru/cat.php')
# listings = parser.get_all_listings(5)
# for listing in listings:
#     print(listing)