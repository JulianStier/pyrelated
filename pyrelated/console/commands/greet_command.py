from cleo.commands.command import Command
from cleo.helpers import argument, option

class GreetCommand(Command):
    name = "greet"
    description = "Greets someone"
    arguments = [
        argument(
            "name",
            description="Who do you want to greet?",
            optional=True
        )
    ]
    options = [
        option(
            "yell",
            "y",
            description="If set, the task will yell in uppercase letters",
            flag=True
        )
    ]

    def handle(self):
        name = self.argument("name")

        if name:
            text = f"Hello {name}"
        else:
            text = "Hello"

        if self.option("yell"):
            text = text.upper()

        self.line(text)
