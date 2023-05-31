import argparse
import re
import requests


class UrlAnalyzer:
    def __new__(cls, *args, **kwargs):
        analyzer = super().__new__(cls)
        if not args and not kwargs:
            analyzer.url = 'https://' + cls.user_input()
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
            url = input('Please set the URL for parsing: https://')
            return url

    def get_links_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return self.link_analyzer.extract_links(response.text)
        else:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return []

    def get_valid_links(self, links):
        return self.link_analyzer.valid_links(links)


class LinkAnalyzer:

    def extract_links(self, text):
        return re.findall(r'https?:\/\/\S+', text)

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
        url_analyzer = UrlAnalyzer()
        links = url_analyzer.get_links_from_url(url_analyzer.url)
        valid_links, not_valid_links = url_analyzer.get_valid_links(links)

        with open("valid_links.txt", "w") as valid_file:
            valid_file.write("\n".join(valid_links))

        with open("broken_links.txt", "w") as broken_file:
            broken_file.write("\n".join(not_valid_links))
    except requests.exceptions.ConnectionError:
        print('It seems you entered wrong site')

