"""
Game Guess Number
This game was created by Sevak Khachatryan
If you find any bugs please write on email example@example.com
"""

import random


def user_guess_number(max_limit):
    """
    The function takes a random number and compares
    it with the number entered by the user
    :param max_limit: maximum digit in range
    :return: integer
    """
    random_number = random.randint(1, max_limit)
    user_input_integer = 0
    while user_input_integer != random_number:
        try:
            user_input_integer = int(input(
                f'Guess a number between 1 and {max_limit}: '
            ))
            if user_input_integer <= 0 or user_input_integer > max_limit:
                print('Sorry, your number doesn\'t meet our requirements')
            elif user_input_integer < random_number:
                print('Sorry, guess again. Too low. ')
            elif user_input_integer > random_number:
                print('Sorry, guess again. Too high. ')
        except ValueError:
            print('Sorry, but you entered word not digit,  idiot')

    print(f'Congrats. You have guessed the number {random_number}'
          f' correctly !!')


def computer_guess_number(max_limit: int) -> int:
    """
    The function generates a number within a given radius
     and depends on the user's response
    :rtype: integer
    :param max_limit: user answer
    :return: integer
    """
    low = 1
    high = max_limit
    feedback = ''
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L),'
                         f' or correct (C): ').lower()
        while feedback != 'h' and feedback != 'l' and feedback != 'c':
            print('Its not valid value, pleas choose (H)-if high,'
                  ' (L)-if low and (C)-if correct')
            feedback = input(f'Is {guess} too high (H), too low (L),'
                             f' or correct (C): ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer guessed your number, {guess}, correctly !!')


# user_guess_number(10)
computer_guess_number(100)
