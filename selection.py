import play_random
import simulated_data

while True:
    print('\nHello, be very watching our minigames\n'
          'At the moment we have two games added :D\n'
          '\nEnter 1 to play simulated data and 2 to play random!\nOr 3 for exit.'.upper())
    try:
        value = input('\n\033[0;35mEnter a number being them\033[0m '
                      '\033[0;32m1, 2\033[0m or \033[0;31m3\033[0m for exit: ')

        while not value.isnumeric():
            value = input('Only number.\nplease: ')
        else:
            number_1 = [1]
            number_2 = [2]
            exit_ = [3]

            if int(value) in number_1:
                print('\nYou chose 1!\nYou will play simulated data :D\n')
                print('Welcome to a data simulator!\n'.upper())
                simulated_data.data_simulator()
            elif int(value) in number_2:
                print('You chose 2!\nYou will play random :D\n')
                print('\nWelcome to play random!\n'.upper())
                play_random.play_random()
            elif int(value) in exit_:
                print('\n♠️Development: Hitalo\n♠️thanks for using :)!'.upper())
                exit()
            else:
                print('Only numbers...')
                continue

    except ValueError:
        print('Não foi possivel')
