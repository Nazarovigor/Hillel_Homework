import pytest
from .analizer import SourceAnalyzer
from .analizer import LinkAnalyzer

@pytest.fixture
def source_analyzer():
    return SourceAnalyzer()

@pytest.fixture
def link_analyzer():
    return LinkAnalyzer()