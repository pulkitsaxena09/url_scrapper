import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

class UrlScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()
        self.extracted_urls = set()

    def get_absolute_url(self, url):
        return urljoin(self.base_url, url)

    def extract_urls(self, soup):
        # Extract URLs from href attributes in anchor tags
        for a_tag in soup.find_all('a', href=True):
            url = self.get_absolute_url(a_tag['href'])
            self.extracted_urls.add(url)
            
        count = 1
        print("\n\n")
        for url in self.extracted_urls:
            print(f"[{count}] {url}")
            count+=1
            
        print("\n\n    [info] Total Unique URLs Found : ", len(self.extracted_urls))

    def save_urls_to_file(self, file_path, file_format='csv'):

        with open(file_path, 'w', newline='') as file:
            if file_format == 'csv':
                writer = csv.writer(file)
                for url in self.extracted_urls:
                    writer.writerow([url])
            elif file_format == 'txt':
                for url in self.extracted_urls:
                    file.write(url + '\n')

