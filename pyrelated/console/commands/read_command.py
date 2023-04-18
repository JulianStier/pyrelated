import os

from cleo.commands.command import Command
from cleo.helpers import argument

from pyrelated.database import Database


class ReadCommand(Command):
    name = "read"
    description = (
        "Read a bibtex file or a yaml file into pyrelated cache for further querying."
    )
    arguments = [argument("path", description="What is the path to your file?")]

    def handle(self):
        path = os.path.expanduser(self.argument("path"))

        if not os.path.exists(path):
            self.line(f"<error>Could not find specified path '{path}'</error>")
            return

        type_db = os.path.splitext(os.path.basename(path))
        assert len(type_db) == 2
        type_db = type_db[1].replace(".", "")

        Database.use(path, type_db)
