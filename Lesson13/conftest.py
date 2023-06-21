import pytest
from analizer import SourceAnalyzer

@pytest.fixture
def source_analyzer():
    return SourceAnalyzer()