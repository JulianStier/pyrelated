import os
import configparser


class Config:
    """
        cfg.get(Config.some_key) == cfg.some_key
    """
    def get(self, key: str):
        raise NotImplementedError()


class DefaultConfig(Config):
    LOCAL_NAME_FILE_CONFIG = ".pyrelated"
    GLOBAL_PATH_CONFIG = os.expanduser("~/.config/pyrelated/")
    GLOBAL_NAME_FILE_CONFIG = ".pyrelated"
    GLOBAL_PATH_CACHE = os.expanduser("~/.cache/pyrelated/")
    LOCAL_NAME_FILE_PROXY_CONFIG = "pyrelated.toml"

    def __getattr__(self, key: str):
        return self.get(key)

    def get(self, key: str):
        name = name.upper().strip()
        return self.__dict__[f"_{name}"]


def yaml():
    proxy = DatabaseProxy("./")
    return proxy.use("yaml")


def bibtex():
    proxy = DatabaseProxy("./")
    return proxy.use("bibtex")

    
def _canonicalize_name(name: str):
    return name.lower().strip()


class Database:
    def use():
        raise NotImplementedError()


class DatabaseProxy:
    def __init__(self, path_data: str):
        pass

    def use(self, name_db: str) -> Database:
        assert name_db is not None
        name_db = _canonicalize_name(name_db)


class YamlDatabase(Database):
    pass


class BibtexDatabase(Database):
    pass
