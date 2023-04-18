from __future__ import annotations

from typing import Iterable

from pyrelated.config import Cfg


class Search:
    @staticmethod
    def driver(config, name) -> Search:
        use_proxy = config.get(Cfg.SCHOLARLY_USEPROXY)
        if use_proxy is None or use_proxy == "False":
            use_proxy = False
        use_proxy = bool(use_proxy)

        if name == "scholarly":
            from pyrelated.search.scholarly import ScholarlySearch

            return ScholarlySearch(use_proxy=use_proxy)
        raise NotImplementedError(
            f"No implementation found for your requested driver '{name}'"
        )

    def search_generic(self, text: str) -> Iterable[Result]:
        raise NotImplementedError()


class LocalSearch(Search):
    def __init__(self, path_local):
        pass

    def search_generic(self, text: str) -> Iterable[Result]:
        pass


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
