from cleo.application import Application

from pyrelated.console.commands.greet_command import GreetCommand

application = Application()
application.add(GreetCommand())

if __name__ == "__main__":
    application.run()
