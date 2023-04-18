from cleo.application import Application

from pyrelated.console.commands.config_command import ConfigCommand
from pyrelated.console.commands.search_command import SearchCommand

application = Application()
application.add(ConfigCommand())
application.add(SearchCommand())

if __name__ == "__main__":
    application.run()
