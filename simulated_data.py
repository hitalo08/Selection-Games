import random
import time


def data_simulator():
    accumulated = 0

    while True:  # loop
        try:
            user_value = input('\nDo you play a cube? yes - no:\nAnswer: ')

            answer_yes = ['yes', 'y', 'Y', 'Yes', 'ye', 'YES', 'Yes', 'YeS', 'yES', 'yEs', 'yeS']
            answer_no = ['no', 'n', 'N', 'No', 'NO', 'nO']

            if user_value in answer_yes:  # check values within the yes or no list
                number_random = random.randint(1, 6)  # generates values from 1 to 6
                print(f'\nThe data has dropped in value: \033[0;35m{number_random}\033[0m')
                accumulated += number_random  # accumulating dice points
                print(f'accumulated points: \033[0;32m{accumulated}\033[0m')
            elif user_value in answer_no:
                print('\nthanks for using'.upper())
                break
            else: # if the value entered is anything other than yes or no, the system asks him to type it again
                print('\ntypes \033[0;33myes\033[0;33m or \033[0;33mno\033[0m')
                continue
        except ValueError:
            print('that number is invalid')
            break
    time.sleep(3)
    value = input('want to continue playing? [s] or anything to go out')
    while value == 's':
        data_simulator()
    else:
        x = True
        while x:
            print('you are leaving the game...')
            x = False
            if x is False:
                break
            else:
                print('incorrect value')

