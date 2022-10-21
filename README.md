<br/>
<p align="center">
  <a href="https://github.com/Davi-S/tic_tac_toe.py-2.0">
    <img src="https://raw.githubusercontent.com/SarvarKh/Tic-Tac-Toe-with_Ruby/master/tic1.gif?raw=true" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TicTacToe v2.0</h3>

  <p align="center">
    The new version of the old TicTacToe. More game options and a lot of fun with a bigger player limit (and more).
    <br/>
    <br/>
    <a href="https://github.com/Davi-S/tic_tac_toe.py-2.0"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/Davi-S/tic_tac_toe.py-2.0">View Demo</a>
    .
    <a href="https://github.com/Davi-S/tic_tac_toe.py-2.0/issues">Report Bug</a>
    .
    <a href="https://github.com/Davi-S/tic_tac_toe.py-2.0/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/Davi-S/tic_tac_toe.py-2.0/total) ![Contributors](https://img.shields.io/github/contributors/Davi-S/tic_tac_toe.py-2.0?color=dark-green) ![Forks](https://img.shields.io/github/forks/Davi-S/tic_tac_toe.py-2.0?style=social) ![Stargazers](https://img.shields.io/github/stars/Davi-S/tic_tac_toe.py-2.0?style=social) ![Issues](https://img.shields.io/github/issues/Davi-S/tic_tac_toe.py-2.0) ![License](https://img.shields.io/github/license/Davi-S/tic_tac_toe.py-2.0) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Authors](#authors)
* [CS50 Final Project](#cs50-final-project)

## About The Project

From the creators of Chess (may not)... It's coming... Tic-to-Tac 2.0!
As the original developers (ancient egyptians) abandoned the project and didn't give us an update for about {2022 - (-1300)} years, I decided to implement some new features by myself on the E-version of the game.

Here is some of the new and upcoming features of the game:
* Wider board.
No more 3x3 boring board, now you can play on a board the size of your monitor with as many squares as you want.
(The size of a square should not be smaller than 3x3 pixels)

* No player limit.
Now you can play with more than two people! No more people waiting in line to play.
(Calm down, you can still play against the computer if you don't have friends)

* More game modes.
Now you can play in:
-teams play
-every man for himself
-multiple games at once
-quickmatch
-puzzes
-and more!

This project is still in development.

Of course, not all features are available yet. But we (only me) are working (weekends only) to make updates available as soon as possible.

If you have thanks, complaints, bugs to report or want to help with development, just contact me.

The GUI is just the terminal for a while.

*western wanted poster*

*GUI developer*

*alive only*

*reward: zero thousand zero hundred and zeroth zero dolars*

## Built With

My hands (no major frameworks used yet)

## Usage

Dowload and run the "app.exe"

## Roadmap

See the [open issues](https://github.com/Davi-S/tic_tac_toe.py-2.0/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/Davi-S/tic_tac_toe.py-2.0/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/Davi-S/tic_tac_toe.py-2.0/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **Davi Sampaio** - *Python developer for 3+ years * - [Davi Sampaio](https://github.com/Davi-S/) - *Made everything*

## CS50 Final Project

This Project was made as the final project of CS50

### What is being approach in this project

#### Matrices relations and patterns

Every matrix is compose of rows, columns, and its intersections, the diagonals. Any of these groups can be found with X and Y axis relation. Find these relations is very important to find patterns and information on each group of the matrix

![image](https://user-images.githubusercontent.com/67160664/197230849-e44591b0-a0e2-4c6c-b173-275aa5e08f0d.png)

The python implementation of this pattern can be found on the "Matrix" class in the "helpers.py" file.

#### Implementation of Minimax algorithm and its variations (AI)

The minimax is a AI algorithm. It is very popular and usefull. Taking a look at the "engine\players.py" file, you can find a implementation of the "minimax" algorithm with "alfa-beta pruning".

Together with the "evaluate function" it can find the best interaction with the matrix. It can be: adding a value on the matrix, finding a combination, excluding information, etc...

#### Usage of the above topics in a TicTacToe engine

Matices and AI can be very powerfull. In this project, I chose to implement a TicTacToe game engine.

The engine is not just a simple 2 player game on a 3x3 board.

The implementation of the "Board Class" allow us to have simple irregular boards, like 3x4 and 8x18; and complex irregular boards, like:

![image](https://user-images.githubusercontent.com/67160664/197236042-8e4aac95-7ed6-414c-aaa6-5157c2487a8b.png)

and still be able to get all information needed; in this case, check for winning patters on the board.

The "WinChecker" class, also can interpret multiple patters on the board and tell if there is a win

The engine, has potential to be inplement in several game modes and even online multiplayer. On the "main.py" and "game_modes.py" file, you can find some simple implementations of game modes and terminal menus

