
from Homework.Lesson13.analizer import SourceAnalyzer


class TestSourceAnalizer:
    def test_get_links_from_url(self, source_analyzer):
        url = "https://google.com"
        links = source_analyzer.get_links_from_url(url)
        assert len(links) > 0

    def test_get_links_from_pdf(self, source_analyzer):
        pdf_path = r"D:\1.pdf"
        links = source_analyzer.get_links_from_pdf(pdf_path)
        assert len(links) > 0

