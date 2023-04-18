import os

from cleo.commands.command import Command
from cleo.helpers import argument, option

from pyrelated.config import Cfg, Config


class ConfigCommand(Command):
    name = "config"
    description = "Displays or modifies configuration of pyrelated"
    arguments = [
        argument(
            "name", description="Which config do you want to modify?", optional=True
        ),
        argument(
            "value", description="What value do you want it set it to?", optional=True
        ),
    ]
    options = [
        option(
            "reset",
            "-R",
            "Reset a single config entry or the whole config back to its default state",
        ),
        option(
            "from",
            "-F",
            "Specify explicitly on which configuration file to operate on",
            flag=False,
        ),
    ]

    def handle(self):
        cfg = Config()
        cfg.load_default()

        path_from = self.option("from")
        if path_from is None:
            path_config_dir = os.path.expanduser(cfg.get(Cfg.PATHS_CONFIG))
            if not os.path.exists(path_config_dir):
                os.makedirs(path_config_dir)
            path_cfg_global = os.path.join(path_config_dir, "pyrelated.toml")

            if os.path.exists(path_cfg_global):
                path_from = path_cfg_global
                cfg.load(path_cfg_global)
            path_target = path_cfg_global

            path_cfg_local = os.path.join(os.getcwd(), cfg.get(Cfg.NAMES_FILES_CONFIG))
            if os.path.exists(path_cfg_local):
                path_from = path_cfg_local
                cfg.load(path_cfg_local)
                path_target = path_cfg_local
        else:
            if not os.path.exists(path_from):
                self.line(
                    f"<error>Could not find path for config '{path_from}'</error>"
                )
                return
            cfg.load(os.path.expanduser(path_from))
            path_target = path_from

        name = self.argument("name")
        if name is None:
            if self.option("reset"):
                if not self.confirm(
                    f"Do you want to reset the whole config to default in file '{path_target}'?",
                    False,
                ):
                    return
                cfg.load_default().save(path_target)
                self.line("Config was reset to default:")

            self.line(f"<info>Config in '{path_from}'</info>")
            for key in cfg.keys():
                self.line(f"\t{key} = {cfg.get(key)}")
            return

        if self.option("reset"):
            val_default = cfg.get_default(name)
            if not self.confirm(
                f"Do you want to reset '{name}' to '{val_default}'?", False
            ):
                return
            cfg.set(name, val_default).save(path_target)
            self.line(f"Resetted {name} to {val_default}")
            return

        value = self.argument("value")
        if value is None:
            try:
                self.line(f"{name} = {cfg.get(name)}")
            except KeyError:
                self.line(f"No such config entry for key '{name}'")
            return

        cfg.set(name, value).save(path_target)
        self.line(f"Updated '{name}' to '{value}'")
