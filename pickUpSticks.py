from time import sleep
import os

def take_sticks(numbOfSticks):
    global user
    sticks = ''
    while numbOfSticks != 0:
        os.system('cls')

        # Print sticks available #
        for _ in range(numbOfSticks):
            sticks += '|'

        print('\n' + sticks)

        # Players turn #
        if user == 'player':
            while True:
                try:
                    prompt = int(input('\nHow many sticks should be removed .. 1, 2, or 3 => '))

                # Data type validation #
                except ValueError:
                    print('\n* Only number input allowed *')
                    sleep(2)
                    continue

                # Number validation #
                if prompt < 1 or prompt > 3:
                    print('\n* Enter 1, 2, or 3 *')
                    sleep(2)
                    continue

                # Make sure enough sticks exist #
                if prompt > numbOfSticks:
                    print('Not enough sticks left:\nSticks left: {}'.format(numbOfSticks))
                    sleep(2)
                    continue

                break

        # Computers turn #
        elif user == 'computer':
            print('\nComputer making decision')
            sleep(2)
            options = [3, 2, 1]
            for option in options:
                if option >= len(sticks):
                    pass                

                elif numbOfSticks in (4,3,2) or numbOfSticks in (6,7,8):
                    if numbOfSticks - option == 1:
                        prompt = option
                        break

                    elif numbOfSticks - option == 5:
                        prompt = option
                        break

                    pass

                else:
                    prompt = option
                    break

        # Print remainder #
        result = (len(sticks) - prompt) * '|'
        numbOfSticks = len(result)
        sleep(2)
        sticks = ''

        # Return loser user #
        if numbOfSticks == 0:
            return user

        # Switch user #
        if user == 'player':
            user = 'computer'
            continue

        elif user == 'computer':
            user = 'player'
            continue

def main():
    global user
    os.system('cls')
    print('''\n                      Rules:
======================================================
 Choose the number of matchsticks (between 5 and 40).
 The computer will decide who goes first ..
 Remove one, two or three matchsticks from the pile. 
 The contestant who removes the last matchstick loses.''')

    # Enter number of sticks #
    try:
        numbOfSticks = int(input('\nEnter a number between 5 and 40 => '))

    # Data type validation #
    except ValueError:
        print('\n* Improper data type entered .. numbers only *')
        sleep(2)
        os.system('cls')
        main()

    # Number validation #
    if 5 > numbOfSticks  or numbOfSticks > 40 :
        print('\n* Enter a correct number in a specified range *')
        sleep(2)
        os.system('cls')
        main()

    # Computer decides who goes first #
    if (numbOfSticks % 4) == 1:
        print('\nPlayers turn')
        sleep(2)
        user = 'player'
        take_sticks(numbOfSticks)
    else:
        print('\nComputers turn')
        sleep(2)
        user = 'computer'
        take_sticks(numbOfSticks)

    # Winner is congratulated #
    if user == 'player':
        print('\nComputer wins!!')
        sleep(2)
    else:
        print('\nPlayer wins!!')
        sleep(2)

    # Play again? #
    while True:
        os.system('cls')
        print('Options:\ny, Y, n, N')
        prompt = input('Play again? => ')

        if prompt in ('y','Y'):
            print('Restarting program ..')
            sleep(2)
            os.system('cls')
            main() 

        elif prompt in ('n','N'):
            print('Exiting ..')
            sleep(2)
            break

        else:
            print('* Choose one of the provided options *')
            sleep(2)
            continue

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('\n\n* Ctrl+C detected .. exiting *')