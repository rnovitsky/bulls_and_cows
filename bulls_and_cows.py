from random import choice
from itertools import permutations


ALL_NUMBERS = [''.join(map(str, number)) for number in permutations(range(10), 4)]
history = []


def bulls_n_cows(number1, number2):
    '''Calculates amounts of bulls and cows between 2 provided numbers'''

    bulls = 0
    for i in range(4):
        if number1[i] == number2[i]:
            bulls += 1
    cows = len(set(number1) & set(number2)) - bulls
    return bulls, cows


def is_compatible(guess):
    '''Checks if provided number is compatible with the data obtained by previous guesses'''

    return all(bulls_n_cows(guess, previous_guess) == (bulls, cows)
        for previous_guess, bulls, cows in history)


def naive_player():
    '''Chooses random numbers from available until a suitable one is not found'''

    while True:
        while True:
            guess = choice(ALL_NUMBERS)
            ALL_NUMBERS.remove(guess)
            if is_compatible(guess):
                break
        print(f'My guess is: {guess}')
        bulls = int(input('Bulls: '))
        if bulls == 4:
            print(f'I won! Your number was {guess}')
            return
        cows = int(input('Cows: '))
        history.append((guess, bulls, cows))


def main():
    answer = input('Do you have any previous guessings?(y/n): ').lower()
    if answer == 'y':
        while True:
            guess = input('Number (leave empty if you have no more guessings): ').strip()
            if guess == '':
                break
            bulls = int(input('Bulls: '))
            cows = int(input('Cows: '))
            if bulls > 4 or cows > 4 or (bulls + cows) > 4:
                print('There can be no more than 4 bulls and cows, read the game rules carefully')
            history.append((guess, bulls, cows))
    naive_player()

if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print('You made a mistake somewhere!')
