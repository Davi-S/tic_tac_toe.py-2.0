"""Menus"""

# IMPORTS #
from abc import ABC
from dataclasses import dataclass
from os import system
from time import sleep

# LOCAL IMPORTS #
import helpers as hp
import settings


PREVIOUS_MENUS: list[str] = []


@dataclass
class Opt:
    name: str
    description: str
    value: dict[callable, dict]
    

def print_options(options: list[Opt]) -> None:
    for idx, value in enumerate(options):
        if value.description:
            print(f"[ {idx+1} ] >>> {value.name} --> {value.description}")
        else:
            print(f"[ {idx+1} ] >>> {value.name}")
    return


def print_title(title: str) -> None:
        print('-' * len(title))
        print(title.upper())
        print('-' * len(title))


class IndependentOptMenu:
    def __init__(self, title: str, options: list[Opt], prompt: str = 'Choose an option: ') -> None:
        self.title = title
        self.options = options
        self.prompt = prompt     
        
    def run(self):  # sourcery skip: for-append-to-extend
        results = []
        while True:
            system('cls')
            print_title(self.title)
            print_options(self.options)
            print()
            option = hp.get_int_max(self.prompt, range(1, len(self.options) + 1))

            if not isinstance(option, int):
                print(option)
                sleep(settings.MEDIUM_SLEEP_TIME)
                continue

            option -= 1
            
            if isinstance(self.options[option].value, str):
                return self.options[option].value
            
            for key, value in self.options[option].value.items():
                results.append(key(**value))
            
            return results
        
    
class IndependentOpenMenu:
    def __init__(self, title: str, text: str, prompt: str) -> None:
        self.title = title
        self.text = text
        self.prompt = prompt

    def run(self) -> str:
        system('cls')
        print_title(self.title)
        print(self.text)
        print()
        return input(self.prompt)


# This abstract canot go to abstracts.py because PREVIOUS_MENUS global
class NestedMenu(ABC):
    def __init__(self, title: str) -> None:
        self.title = title
        
    def print_title(self):
        chars = sum(len(char) for char in PREVIOUS_MENUS) + len(self.title) + 3 * len(PREVIOUS_MENUS)
        print('-' * chars)
        for name in PREVIOUS_MENUS:
            print(f'{name.lower()} → ', end='')
        print(self.title.upper())
        print('-' * chars)


class NestedOptionMenu(NestedMenu):
    def __init__(self, title: str, options: list[Opt], prompt: str = 'Choose an option: ', one_time: bool = False) -> None:
        super().__init__(title)
        self.options = options
        self.prompt = prompt
        # one_time is used to skip the previous menu
        self.one_time = one_time

    def run(self) -> str:
        while True:
            system('cls')
            self.print_title()
            print_options(self.options)
            print()
            option = hp.get_int_max(self.prompt, range(1, len(self.options) + 1))

            if not isinstance(option, int):
                print(option)
                sleep(settings.MEDIUM_SLEEP_TIME)
                continue

            option -= 1

            if self.options[option].value is None:
                system('cls')
                print(
                    f'| {self.options[option].name} | is not implemented yet')
                sleep(settings.MEDIUM_SLEEP_TIME)
                continue
            
            # back to previous menu
            if self.options[option].value == 'return':
                return

            PREVIOUS_MENUS.append(self.title)
            
            for key, value in self.options[option].value.items():
                key(**value)
        
            # back to pre-previous menu
            if self.one_time:
                PREVIOUS_MENUS.pop()
                return
            
            PREVIOUS_MENUS.pop()

class NestedOpenMenu(NestedMenu):
    def __init__(self, title: str, text: str, prompt: str) -> None:
        super().__init__(title)
        self.text = text
        self.prompt = prompt

    def run(self) -> str:
        system('cls')
        self.print_title()
        print(self.text)
        print()
        return input(self.prompt)


def main() -> int:
    return 0


if __name__ == '__main__':
    main()
