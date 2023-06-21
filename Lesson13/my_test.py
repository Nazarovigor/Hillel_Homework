import pytest
from analizer import SourceAnalyzer

def test_get_links_from_url(source_analyzer):
    url = "https://google.com"
    links = source_analyzer.get_links_from_url(url)
    assert len(links) > 0

def test_get_links_from_pdf(source_analyzer):
    pdf_path = r"D:\1.pdf"
    links = source_analyzer.get_links_from_pdf(pdf_path)
    assert len(links) > 0

