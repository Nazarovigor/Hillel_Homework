import os
import logging
import pytest
import requests
from Homework.Lesson13.analizer import SourceAnalyzer
from Homework.Lesson13.analizer import LinkAnalyzer


class TestSourceAnalizer:
    @pytest.mark.smoke
    def test_get_links_from_url(self):
        url = "https://google.com"
        source_analyzer = SourceAnalyzer(url)
        logging.info("start get links from url")
        links = source_analyzer.get_links_from_url(url)
        logging.info("fnish get links from url")
        assert len(links) > 0

    @pytest.mark.smoke
    def test_get_links_from_pdf(self):
        pdf_path = r"../1.pdf"
        source_analyzer = SourceAnalyzer(pdf=pdf_path)
        logging.info("start get links from pdf")
        links = source_analyzer.get_links_from_pdf(pdf_path)
        logging.info("finish get links from pdf")
        assert len(links) > 0

    @pytest.mark.regress
    def test_get_valid_links_from_url(self):
        url = "https://google.com"
        source_analyzer = SourceAnalyzer(url)
        logging.info("start get valid links from url")
        links = source_analyzer.get_links_from_url(url)
        valid_links = source_analyzer.get_valid_links(links)
        logging.info("finish get valid links from url")
        assert len(valid_links) > 0

    @pytest.mark.regress
    def test_get_valid_links_from_pdf(self):
        path = r"../1.pdf"
        source_analyzer = SourceAnalyzer(pdf=path)
        links = source_analyzer.get_links_from_pdf(path)
        logging.info("start get valid links from pdf")
        valid_links = source_analyzer.get_valid_links(links)
        logging.info("finish get valid links from pdf")
        assert len(valid_links) > 0

    @pytest.mark.regress
    def test_get_not_valid_links_from_pdf(self):
        path = r"../1.pdf"
        source_analyzer = SourceAnalyzer(pdf=path)
        links = source_analyzer.get_links_from_pdf(path)
        logging.info("start get not valid links from pdf")
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        logging.info("finish get not valid links from pdf")
        assert len(not_valid_links) > 0

    @pytest.mark.regress
    def test_get_not_valid_links_from_url(self):
        url = "http://the-internet.herokuapp.com/status_codes"
        source_analyzer = SourceAnalyzer(url)
        links = source_analyzer.get_links_from_url(url)
        logging.info("start get not valid links from url")
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        logging.info("finish get not valid links from url")
        assert len(not_valid_links) > 0

    @pytest.mark.smoke
    def test_valid_links_writer(self):
        url = "https://google.com"
        source_analyzer = SourceAnalyzer(url)
        links = source_analyzer.get_links_from_url(url)
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        logging.info("start write")
        source_analyzer.links_writer(valid_links, not_valid_links)
        logging.info("finish write")
        assert os.path.isfile('valid_links.txt')

    @pytest.mark.smoke
    def test_not_valid_links_writer(self):
        url = "https://google.com"
        source_analyzer = SourceAnalyzer(url)
        links = source_analyzer.get_links_from_url(url)
        valid_links, not_valid_links = source_analyzer.get_valid_links(links)
        logging.info("start write")
        source_analyzer.links_writer(valid_links, not_valid_links)
        logging.info("finish write")
        assert os.path.isfile('broken_links.txt')

    @pytest.mark.regress
    def test_extract_links_from_url(self):
        url = "https://google.com"
        link_analyzer = LinkAnalyzer()
        response = requests.get(url)
        logging.info("start extract links from url")
        links = link_analyzer.extract_links_form_url(response.text, url)
        logging.info("finish extract links from url")
        assert len(links) > 0

    @pytest.mark.regress
    def test_extract_links_from_pdf(self):
        path = r"../1.pdf"
        link_analyzer = LinkAnalyzer()
        logging.info("start extract links from pdf")
        links = link_analyzer.extract_links_from_pdf(path)
        logging.info("finish extract links from pdf")
        assert len(links) > 0