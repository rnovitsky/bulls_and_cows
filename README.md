# Bulls and Cows Solver

## Overview
This script is intended to automate guessing in a popular game [Bulls and Cows](https://en.wikipedia.org/wiki/Bulls_and_Cows).

You can play the online version of this game [here](https://www.mathsisfun.com/games/bulls-and-cows.html).

## Game rules
* Number always contains 4 digits
* No repeating digits
* Leading zero is allowed
* Number of guessing attempts is not limited

## Algorithm
1. One of the available numbers is randomly chosen
2. The number is compared with the previous guesses to have the same amount of bulls and cows
3. If number is compatible with all assumptions from history it is shown to the player
4. Player marks amount of bulls and cows
5. Results are saved to the history

## How to run
```
python bulls_and_cows.py
```