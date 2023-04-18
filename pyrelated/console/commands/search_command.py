import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

from pyrelated.config import Cfg, Config
from pyrelated.search import Search


class SearchCommand(Command):
    name = "search"
    description = "Search for bibliography through a proxy such as gscholar"
    arguments = [argument("query", description="What is your search query?")]
    options = [
        option(
            "driver",
            "D",
            description="Name of your desired driver",
            flag=False,
        ),
        option(
            "config",
            "C",
            description="Path to configuration",
            flag=False,
        ),
    ]

    def handle(self):
        cfg = Config()
        cfg.load_default()

        cfg_path_from = self.option("config")
        if cfg_path_from is None:
            path_config_dir = os.path.expanduser(cfg.get(Cfg.PATHS_CONFIG))
            if not os.path.exists(path_config_dir):
                os.makedirs(path_config_dir)
            path_cfg_global = os.path.join(path_config_dir, "pyrelated.toml")

            if os.path.exists(path_cfg_global):
                # cfg_path_from = path_cfg_global
                cfg.load(path_cfg_global)
            # cfg_path_target = path_cfg_global

            path_cfg_local = os.path.join(os.getcwd(), cfg.get(Cfg.NAMES_FILES_CONFIG))
            if os.path.exists(path_cfg_local):
                # cfg_path_from = path_cfg_local
                cfg.load(path_cfg_local)
                # cfg_path_target = path_cfg_local
        else:
            if not os.path.exists(cfg_path_from):
                self.line(
                    f"<error>Could not find path for config '{cfg_path_from}'</error>"
                )
                return
            cfg.load(os.path.expanduser(cfg_path_from))
            # cfg_path_target = cfg_path_from

        query = self.argument("query")
        driver = self.option("driver")
        if driver is None:
            driver = "scholarly"

        searcher = Search.driver(cfg, driver)
        for result in searcher.search_generic(query):
            self.line(result)
