"""User Interface"""

# IMPORTS #
from textual.app import App
from textual.widget import Widget
from textual.widgets import Placeholder, Button

# LOCAL IMPORTS #

# LOGGING IMPORTS #
from logs.logging_configuration import create_file_handler
import logging
# Get the file logger and its handler
_log = logging.getLogger(__name__)
_log.addHandler(create_file_handler(__name__))


class MainApp(App):
     async def on_mount(self) -> None:
        await self.view.dock(Placeholder(name="header"), edge="top", size=3)
        await self.view.dock(Placeholder(name="footer"), edge="bottom", size=3)
        await self.view.dock(Placeholder(name="stats"), edge="left", size=40)
        await self.view.dock(Placeholder(name="message"), edge="right", size=40)
        await self.view.dock(Placeholder(name="grid"), edge="top")


def main() -> int:
    MainApp.run()
    return 0


if __name__ == '__main__':
    main()