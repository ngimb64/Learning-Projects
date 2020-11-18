from turtle import color, begin_fill, forward, left, end_fill, clear
import sys

def num_input(message):
    while True:
        try:
            num = int(input(message))
            if 0 == num or num > 10:
                print('* Pick a number between 1 and 10 *')
                continue
            elif 1 <= num <= 10:
                return num
        except ValueError:
            print('* Enter integer(#) data type *')

def handled_input(message, dataset):
    while True:
        choice = str(input(message))

        for data in dataset:
            if choice != data:
                pass
            else:
                return choice

        print('* Enter one of the options provided *')
        print(dataset)
        continue

def main():
    colors = ['green', 'yellow', 'blue', 'black', 'red', 'orange']
    prompt = num_input('Enter the number of sides to draw: ')
    shade = handled_input('Enter the color of the shape: ', colors)

    color('black', shade)
    begin_fill()

    for _ in range(prompt):
        forward(100)
        left(360/prompt)

    end_fill()

    yay_nay = ['y','n']
    choice = handled_input('Would you like to reset the canvas? ', yay_nay)
    if choice == 'n':
        sys.exit(0)

    clear()
    main()

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print('Ctrl+C detected .. exiting')