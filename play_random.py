import random, time


def play_random():

    while True:

        value_random = random.randint(1, 20) # generates values from 1 to 20
        user_input = input('Please, insert a number: ')

        #  as long as what the user enters is not a number, the system will ask to enter it again
        while not user_input.isnumeric():
            user_input = input('Only numbers.\nnumber:')
        else:
            user_input = int(user_input)
            if user_input == value_random:  # if the value that the user enters is equal to the random value, he will receive a message saying he was right
                print(f'\nYou got the value right!\nThe value is: \033[0;35m{user_input}\033[0m.')
                break
            elif user_input > value_random:  # if value greater than the generating random value
                print('\n\033[0;36mThe value entered is greater!\033[0m\n')
            elif user_input < value_random:  # if value less than the generating  random value
                print('\n\033[0;36mThe value entered is less!\033[0m\n')
            else:
                print('incorrect value')
                break
    time.sleep(3)
    value = input('want to continue playing? [s] or anything to go out: ')
    while value == 's':
        play_random()
    else:
        x = True
        while x:
            print('you are leaving the game...')
            x = False
            if x is False:
                break
            else:
                print('incorrect value')


