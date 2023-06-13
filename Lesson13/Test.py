import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class UrlAnalyzer:
    def __new__(cls, *args, **kwargs):
        analyzer = super().__new__(cls)
        if not args and not kwargs:
            analyzer.url = cls.user_input()
        return analyzer

    def __init__(self, url=None):
        if url:
            self.url = url
        self.link_analyzer = LinkAnalyzer()

    @staticmethod
    def user_input():
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', type=str, help='Please set the URL for parsing')
        args = parser.parse_args()
        if args.url:
            return args.url
        else:
            url = input('Please set the URL for parsing starting from http or https: ')
            if url.startswith('http://') or url.startswith('https://'):
                return url
            else:
                print('Invalid URL format. Please start with http:// or https://')
                return UrlAnalyzer.user_input()

    def get_links_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return self.link_analyzer.extract_links(response.text, url)
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return []

    def get_valid_links(self, links):
        return self.link_analyzer.valid_links(links)

    @staticmethod
    def links_writer(valid_links, not_valid_links):
        with open("valid_links.txt", "w") as valid_file:
            valid_file.write("\n".join(valid_links))

        with open("broken_links.txt", "w") as broken_file:
            broken_file.write("\n".join(not_valid_links))


class LinkAnalyzer:
    def extract_links(self, text, base_url):
        soup = BeautifulSoup(text, 'html.parser')
        links = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)  # Объединение относительной ссылки с базовым URL
                links.append(full_url)

        return links

    @staticmethod
    def valid_links(links):
        valid_links = []
        not_valid_links = []
        for link in links:
            response = requests.get(link)
            if response.status_code == 200:
                valid_links.append(link)
            else:
                not_valid_links.append(link)
        return valid_links, not_valid_links


if __name__ == "__main__":
    try:
        analizer = UrlAnalyzer()
        links = analizer.get_links_from_url(analizer.url)
        valid_links, not_valid_links = analizer.get_valid_links(links)
        analizer.links_writer(valid_links, not_valid_links)
    except requests.exceptions.ConnectionError:
        print('It seems you entered the wrong site')
    except requests.exceptions.InvalidURL:
        print('It seems you entered the wrong site')

