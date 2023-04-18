from __future__ import annotations

from scholarly import ProxyGenerator, scholarly

from pyrelated.search.base import Result, Search


class ScholarlySearch(Search):
    def __init__(self, use_proxy: bool = True, proxy_generator=None):
        if use_proxy:
            self._pg = ProxyGenerator() if proxy_generator is None else proxy_generator
            success = self._pg.FreeProxies()
            if success:
                scholarly.use_proxy(self._pg)

    def search_generic(self, text: str):
        # query_result = scholarly.search_pubs(text)
        query_result = {
            "author_id": ["4bahYMkAAAAJ", "ruUKktgAAAAJ", ""],
            "bib": {
                "abstract": "Humans can judge from vision alone whether an object is "
                "physically stable or not. Such judgments allow observers "
                "to predict the physical behavior of objects, and hence "
                "to guide their motor actions. We investigated the visual "
                "estimation of physical stability of 3-D objects (shown "
                "in stereoscopically viewed rendered scenes) and how it "
                "relates to visual estimates of their center of mass "
                "(COM). In Experiment 1, observers viewed an object near "
                "the edge of a table and adjusted its tilt to the "
                "perceived critical angle, ie, the tilt angle at which "
                "the object",
                "author": ["SA Cholewiak", "RW Fleming", "M Singh"],
                "pub_year": "2015",
                "title": "Perception of physical stability and center of mass of 3-D "
                "objects",
                "venue": "Journal of vision",
            },
            "citedby_url": "/scholar?cites=15736880631888070187&as_sdt=5,33&sciodt=0,33&hl=en",
            "eprint_url": "https://jov.arvojournals.org/article.aspx?articleID=2213254",
            "filled": False,
            "gsrank": 1,
            "num_citations": 23,
            "pub_url": "https://jov.arvojournals.org/article.aspx?articleID=2213254",
            "source": "PUBLICATION_SEARCH_SNIPPET",
            "url_add_sclib": "/citations?hl=en&xsrf=&continue=/scholar%3Fq%3DPerception%2Bof%2Bphysical%2Bstability%2Band%2Bcenter%2Bof%2Bmass%2Bof%2B3D%2Bobjects%26hl%3Den%26as_sdt%3D0,33&citilm=1&json=&update_op=library_add&info=K8ZpoI6hZNoJ&ei=QhqhX66wKoyNy9YPociEuA0",
            "url_scholarbib": "/scholar?q=info:K8ZpoI6hZNoJ:scholar.google.com/&output=cite&scirp=0&hl=en",
        }
        yield self._return_lightweight(query_result)

    def _return_lightweight(self, results):
        for entry in results:
            result = Result()
            result.author_gids = entry["author_id"] if "author_id" in entry else []
            result.author_names = (
                entry["bib"]["author"]
                if "bib" in entry and "author" in entry["bib"]["author"]
                else []
            )
            result.abstract = (
                entry["bib"]["abstract"]
                if "bib" in entry and "abstract" in entry["bib"]["abstract"]
                else ""
            )
            result.num_citations = (
                int(entry["num_citations"]) if "num_citations" in entry else None
            )
            yield result
