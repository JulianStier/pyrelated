import pytest

from pyrelated.search.scholarly import ScholarlySearch


@pytest.mark.skip("Currently ignored as it uses an expensive proxy call")
def test_search_scholarly_generic():
    searcher = ScholarlySearch()
    searcher.search_generic("Albert Einstein")
