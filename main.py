import argparse
from URL_Scrapper import UrlScraper
import requests
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(description='Web scraper for extracting and saving URLs.')
    parser.add_argument('url', help='The URL to scrape')
    parser.add_argument('-oFR','--output-format', choices=['csv', 'txt'], default='csv', help='Output format (csv or txt)')
    parser.add_argument('-oFL','--output-file', required=True, help='Output file path')

    args = parser.parse_args()

    scraper = UrlScraper(args.url)
    response = requests.get(args.url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        scraper.extract_urls(soup)

        scraper.save_urls_to_file(args.output_file, args.output_format)
        print(f"URLs saved to {args.output_file}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()
