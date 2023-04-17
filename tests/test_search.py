from pyrelated.search import ScholarlySearch


def test_search_scholarly_generic():
    searcher = ScholarlySearch()
    searcher.search_generic("Albert Einstein")
