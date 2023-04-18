import configparser
import os

from pyrelated import __version__


def merge(a: dict, b: dict, path: list = None):
    if path is None:
        path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge(a[key], b[key], path + [str(key)])
            elif a[key] != b[key]:
                a[key] = b[key]  # Overwriting from b
        else:
            a[key] = b[key]
    return a


def flatten(a: dict, prefix: str = None, path: list = None) -> dict:
    f = dict()
    if path is None:
        path = [] if prefix is None else [prefix]
    crumbles = ".".join(path)
    for key in a:
        if isinstance(a[key], dict):
            f.update(flatten(a[key], prefix=None, path=path + [str(key)]))
        else:
            if len(path) > 0:
                if crumbles not in f:
                    f[crumbles] = {}
                f[crumbles][key] = a[key]
            else:
                f[key] = a[key]
    return f


def old_flatten(a: dict, prefix: str = None, path: list = None) -> dict:
    f = dict()
    if path is None:
        path = [] if prefix is None else [prefix]
    crumbles = ".".join(path)
    for key in a:
        if isinstance(a[key], dict):
            f.update(old_flatten(a[key], prefix=None, path=path + [str(key)]))
        else:
            fkey = key
            if len(path) > 0:
                fkey = crumbles + "." + key
            f[fkey] = a[key]
    return f


class Cfg:
    NAMES_FILES_CONFIG = "names_files_config"
    PATHS_CONFIG = "paths_config"
    SCHOLARLY_USEPROXY = "scholarly_useproxy"


class Config:
    """
    cfg.get(Config.some_key) == cfg.some_key
    """

    _default_config: dict = {
        "local": {
            "names": {
                "files": {"config": ".pyrelated", "proxyconfig": "pyrelated.toml"}
            }
        },
        "global": {
            "version": __version__.version,
            "paths": {
                "config": os.path.expanduser("~/.config/pyrelated/"),
                "cache": os.path.expanduser("~/.cache/pyrelated/"),
            },
            "scholarly": {"useproxy": False},
            "names": {"files": {"config": ".pyrelated"}},
        },
    }

    def __init__(self):
        self._config = configparser.ConfigParser()

    def keys(self):
        for sec in self._config:
            for key in self._config[sec]:
                path = sec.replace("pyrelated.", "")
                path = path.replace("pyrelated", "")
                path = path.replace(".", "_")
                yield path + "_" + key if len(path) > 0 else key

    def load_default(self):
        # First use global config values
        conf = self._default_config["global"]

        # Second merge local
        merge(conf, self._default_config["local"])

        flattened = flatten(conf, prefix="pyrelated")
        for path in flattened:
            self._config[path] = flattened[path]

        return self

    def update(self, config: dict, path: list = None):
        if path is None:
            path = []
        for key in config:
            pass

    def load(self, path):
        assert os.path.exists(path)
        self._config.read(path)
        assert "pyrelated" in self._config
        return self

    def get(self, key: str):
        query = key.split("_")
        key = query[-1]
        path = "pyrelated." + ".".join(query[:-1]) if len(query) > 1 else "pyrelated"
        return self._config[path][key]

    def get_default(self, key: str):
        # First use global config values
        conf = self._default_config["global"]
        # Second merge local
        merge(conf, self._default_config["local"])
        flattened = flatten(conf, prefix="pyrelated")

        query = key.split("_")
        key = query[-1]
        path = "pyrelated." + ".".join(query[:-1]) if len(query) > 1 else "pyrelated"

        return flattened[path][key]

    def set(self, key: str, value):
        query = key.split("_")
        key = query[-1]
        path = "pyrelated." + ".".join(query[:-1]) if len(query) > 1 else "pyrelated"
        self._config[path][key] = value
        return self

    def save(self, path):
        path_base = os.path.dirname(path)
        if len(path_base) > 0 and not os.path.exists(path_base):
            os.makedirs(path_base)
        with open(path, "w+") as handle:
            self._config.write(handle)
