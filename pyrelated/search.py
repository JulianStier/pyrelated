from scholarly import ProxyGenerator, scholarly


class Result:
    author_gids: list
    author_names: list
    abstract: str
    _is_lightweight: bool = True

    @property
    def lightweight(self):
        return self._is_lightweight

    @lightweight.setter
    def lightweight(self, flag):
        self._is_lightweight = bool(flag)


class Search:
    def search_generic(self, text: str):
        raise NotImplementedError()


class ScholarlySearch:
    def __init__(self, use_proxy: bool = True, proxy_generator=None):
        if use_proxy:
            self._pg = ProxyGenerator() if proxy_generator is None else proxy_generator
            success = self._pg.FreeProxies()
            if success:
                scholarly.use_proxy(self._pg)

    def search_generic(self, text: str):
        query_result = scholarly.search_pubs(text)
        return self._return_lightweight(query_result)

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
