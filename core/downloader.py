import os
import requests
from concurrent.futures import ThreadPoolExecutor

class ImageDownloader:
    def __init__(self, urls, save_directory='downloads', max_workers=5):
        self.urls = urls
        self.save_directory = save_directory
        self.max_workers = max_workers

        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def download_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            filename = os.path.join(self.save_directory, os.path.basename(url))
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Successfully downloaded {url} to {filename}')
        except requests.RequestException as e:
            print(f'Failed to download {url}: {e}')

    def download_images(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self.download_image, self.urls)

# Example usage:
# urls = ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']
# downloader = ImageDownloader(urls)
# downloader.download_images()