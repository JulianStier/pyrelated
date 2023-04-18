from __future__ import annotations

from pyrelated.search.base import Result


def yaml():
    return Database.use("yaml")


def bibtex():
    return Database.use("bibtex")


def _canonicalize_name(name: str):
    return name.lower().strip()


class Database:
    @staticmethod
    def use(path_data: str, name_db: str) -> Database:
        assert name_db is not None
        name_db = _canonicalize_name(name_db)

        if name_db == "yaml":
            return YamlDatabase(path_data)
        elif name_db == "bibtex":
            return BibtexDatabase(path_data)

        raise NotImplementedError(
            f"No implementation for the requested db type {name_db} available."
        )

    def add(self, result: Result):
        raise NotImplementedError()

    def contains(self, result: Result) -> bool:
        raise NotImplementedError()

    def categories(self) -> list:
        raise NotImplementedError()

    def has_category(self, name: str) -> bool:
        raise NotImplementedError()

    def add_category(self, name: str):
        raise NotImplementedError()


class YamlDatabase(Database):
    def __init__(self, path: str):
        pass


class BibtexDatabase(Database):
    def __init__(self, path: str):
        pass
