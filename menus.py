"""Recursive menus"""

# IMPORTS #
from abc import ABC
from dataclasses import dataclass
from os import system
from time import sleep


# LOCAL IMPORTS #
from helpers import get_int_max
import settings

PREVIOUS_MENUS: list[str] = []


@dataclass
class Opt:
    name: str
    description: str
    value: dict[callable, dict]


class Menu(ABC):
    def __init__(self, title: str, prompt: str) -> None:
        self.title = title
        self.prompt = prompt

    def print_title(self):
        chars = sum(len(char) for char in PREVIOUS_MENUS) + len(self.title) + 3 * len(PREVIOUS_MENUS)
        print('-' * chars)
        for name in PREVIOUS_MENUS:
            print(f'{name.lower()} → ', end='')
        print(self.title.upper())
        print('-' * chars)


class OptionMenu(Menu):
    def __init__(self, title: str, options: list[Opt], prompt: str = 'Choose a option: ', one_time: bool = False) -> None:
        super().__init__(title, prompt)
        self.options = options
        
        # one_time is used to skip the previous menu
        self.one_time = one_time
    
    def print_options(self) -> None:
        for idx, value in enumerate(self.options):
            if value.description:
                print(f"[ {idx+1} ] >>> {value.name} --> {value.description}")
            else:
                print(f"[ {idx+1} ] >>> {value.name}")
        return

    def run(self) -> str:
        while True:
            system('cls')
            self.print_title()
            self.print_options()
            print()
            option = get_int_max(self.prompt, range(1, len(self.options) + 1))

            if not isinstance(option, int):
                print(option)
                sleep(settings.SLEEP_TIME)
                continue

            option -= 1

            # back to previous menu
            if self.options[option].value == 'return':
                return

            if isinstance(self.options[option].value, str):
                system('cls')
                print(
                    f'| {self.options[option].name} | is not implemented yet')
                sleep(settings.SLEEP_TIME)
                continue

            PREVIOUS_MENUS.append(self.title)
            
            for key, value in self.options[option].value.items():
                key(**value)
        
            # back to pre-previous menu
            if self.one_time:
                PREVIOUS_MENUS.pop()
                return
            
            PREVIOUS_MENUS.pop()

class OpenMenu(Menu):
    def __init__(self, title: str, text: str, prompt: str) -> None:
        super().__init__(title, prompt)
        self.text = text

    def run(self) -> str:
        system('cls')
        self.print_title()
        print(self.text)
        print()
        return input(self.prompt)


def main() -> int:
    menu = OptionMenu('title', [Opt('name1', 'desc1', 'callable1'), Opt(
        'name2', 'desc2', 'callable2'), Opt('name3', '', 'callable3')], 'prompt')
    menu.run()
    return 0


if __name__ == '__main__':
    main()
