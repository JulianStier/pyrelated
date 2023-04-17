from pyrelated.search import Result


def yaml():
    proxy = DatabaseProxy("./")
    return proxy.use("yaml")


def bibtex():
    proxy = DatabaseProxy("./")
    return proxy.use("bibtex")


def _canonicalize_name(name: str):
    return name.lower().strip()


class Database:
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


class DatabaseProxy:
    def __init__(self, path_data: str):
        self._path = path_data

    def use(self, name_db: str) -> Database:
        assert name_db is not None
        name_db = _canonicalize_name(name_db)

        match name_db:
            case "yaml":
                return YamlDatabase(self._path)
            case "bibtex":
                return BibtexDatabase(self._path)


class YamlDatabase(Database):
    def __init__(self, path: str):
        pass


class BibtexDatabase(Database):
    def __init__(self, path: str):
        pass
