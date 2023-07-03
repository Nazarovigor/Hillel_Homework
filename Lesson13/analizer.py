import argparse
import re
import PyPDF2 as PyPDF2
import requests
import os
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin

logging.basicConfig(filename='myLog.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s -- %(levelname)s -- %(message)s')


class SourceAnalyzer:
    def __new__(cls, *args, **kwargs):
        analyzer = super().__new__(cls)
        if not args and not kwargs:
            logging.info(f'user enters parametr')
            analyzer.param = cls.user_input()
        return analyzer

    def __init__(self, url=None, pdf=None):
        if url:
            self.url = url
        if pdf:
            self.pdf = pdf
        self.link_analyzer = LinkAnalyzer()

    @staticmethod
    def user_input():
        parser = argparse.ArgumentParser()
        parser.add_argument('-url', '--URL', type=str, default=None,
                            help='Please set the URL for parsing starting from http or https')
        parser.add_argument('-pdf', '--PDF', type=str, default=None, help='Please set the path to pdf file')
        args = parser.parse_args()
        logging.info('start enter parametr.')
        if args.URL:
            logging.info('The recieve URL')
            return args.URL
        elif args.PDF:
            logging.info('The recieve PDF')
            return args.PDF
        else:
            return None

    def get_links_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return self.link_analyzer.extract_links_form_url(response.text, url)
        else:
            logging.critical('Not valid URL', exc_info=True)
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return []

    def get_links_from_pdf(self, path):
        if os.path.isfile(path):
            return self.link_analyzer.extract_links_from_pdf(path)
        else:
            logging.critical('Invalid path to pdf file', exc_info=True)
            print('Invalid path to pdf file')
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
    def extract_links_form_url(self, text, base_url):
        soup = BeautifulSoup(text, 'html.parser')
        links = []

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                full_url = urljoin(base_url, href)  # Объединение относительной ссылки с базовым URL
                links.append(full_url)

        return links

    def extract_links_from_pdf(self, path):
        with open(path, 'rb') as file:
            logging.info('Start extracting lnks from pdf')
            pdf_reader = PyPDF2.PdfReader(file)
            links = []

            for page in range(len(pdf_reader.pages)):
                current_page = pdf_reader.pages[page]
                page_text = current_page.extract_text()
                page_text = page_text.split(' ')
                page_text = ''.join(page_text)
                url_pattern = re.compile(r'(https?://\S+[^\s\"\)\,\.])')
                found_urls = re.findall(url_pattern, page_text)
                links.extend(found_urls)

            return links

    @staticmethod
    def valid_links(links):
        valid_links = []
        not_valid_links = []
        for link in links:
            try:
                response = requests.get(link)
                if response.status_code == 200:
                    logging.info('Writing url to valid')
                    valid_links.append(link)
                else:
                    logging.info('Writing url to not valid')
                    not_valid_links.append(link)
            except requests.exceptions.ConnectionError:
                logging.warning('ConnectionError, writing url to not valid')
                not_valid_links.append(link)
            except requests.exceptions.InvalidURL:
                logging.warning('InvalidURL, writing url to not valid')
                not_valid_links.append(link)
        return valid_links, not_valid_links


if __name__ == "__main__":
    analizer = None
    while True:
        if analizer is None:
            analizer = SourceAnalyzer()
            if analizer.param is None:
                print("Вы не ввели аргументы. Попробуйте снова.")
                analizer.param = input('Введите параметры: ')
                if analizer.param == "":
                    analizer = None
                    continue

        try:
            if analizer.param.startswith('http://') or analizer.param.startswith('https://'):
                logging.info('start parsing url')
                links = analizer.get_links_from_url(analizer.param)
                valid_links, not_valid_links = analizer.get_valid_links(links)
                analizer.links_writer(valid_links, not_valid_links)
                break
            elif os.path.isfile(analizer.param):
                logging.info('start parsing pdf')
                links = analizer.get_links_from_pdf(analizer.param)
                valid_links, not_valid_links = analizer.get_valid_links(links)
                analizer.links_writer(valid_links, not_valid_links)
                break
            elif analizer.param == "":
                logging.critical('The user did not enter a parameter')
                print('Вы не ввели никаких аргументов')
            else:
                logging.critical('The user did not enter parameter or entered wrong data')
                print('Некорректный формат URL или путь к файлу PDF')
                analizer = None  # Сбрасываем analizer на None, чтобы повторно предложить ввести аргумент

        except requests.exceptions.ConnectionError:
            logging.critical('ConnectionError', exc_info=True)
            print('Похоже, вы ввели неправильный сайт')
            break
        except requests.exceptions.InvalidURL:
            logging.critical('Not valid URL', exc_info=True)
            print('Похоже, вы ввели неправильный сайт')
            break
        except AttributeError:
            logging.critical('No attribute', exc_info=True)
            print('Похоже, вы не ввели атрибут')
            analizer = None
