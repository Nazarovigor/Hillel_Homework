import os
import requests
from Homework.Lesson13.analizer import SourceAnalyzer


class TestSourceAnalizer:
    def test_get_links_from_url(self, source_analyzer):
        url = "https://google.com"
        links = source_analyzer.get_links_from_url(url)
        assert len(links) > 0

    def test_get_links_from_pdf(self, source_analyzer):
        pdf_path = r"../1.pdf"
        links = source_analyzer.get_links_from_pdf(pdf_path)
        assert len(links) > 0

    def test_get_valid_links_from_url(self, source_analyzer):
        url = "https://google.com"
        links = source_analyzer.get_links_from_url(url)
        valid_links = source_analyzer.get_valid_links(links)
        assert len(valid_links) > 0

    def test_get_valid_links_from_pdf(self, source_analyzer):
        path = r"../1.pdf"
        links = source_analyzer.get_links_from_pdf(path)
        valid_links = source_analyzer.get_valid_links(links)
        assert len(valid_links) > 0

    def test_get_not_valid_links_from_pdf(self, source_analyzer):
        path = r"../1.pdf"
        links = source_analyzer.get_links_from_pdf(path)
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        assert len(not_valid_links) > 0


    def test_get_not_valid_links_from_url(self, source_analyzer):
        url = "http://the-internet.herokuapp.com/status_codes"
        links = source_analyzer.get_links_from_url(url)
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        assert len(not_valid_links) > 0

    def test_valid_links_writer(self, source_analyzer):
        url = "https://google.com"
        links = source_analyzer.get_links_from_url(url)
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        source_analyzer.links_writer(valid_links, not_valid_links)
        assert os.path.isfile('valid_links.txt')

    def test_not_valid_links_writer(self, source_analyzer):
        url = "https://google.com"
        links = source_analyzer.get_links_from_url(url)
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        source_analyzer.links_writer(valid_links, not_valid_links)
        assert os.path.isfile('broken_links.txt')

    def test_extract_links_from_url(self, link_analyzer):
        url = "https://google.com"
        response = requests.get(url)
        links = link_analyzer.extract_links_form_url(response.text, url)
        assert len(links) > 0

    def test_extract_links_from_pdf(self, link_analyzer):
        path = r"../1.pdf"
        links = link_analyzer.extract_links_from_pdf(path)
        assert len(links) > 0