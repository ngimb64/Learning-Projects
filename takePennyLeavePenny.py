# Function ensures users enters a number from 1 to 99 #
def input_range(message):
    while True:
        try:
            user_input = int(input(message))
            if user_input < 1:
                print('Please enter between 1 and 99 cents')
                continue
            if user_input > 99:
                print('Please enter between 1 and 99 cents')
                continue
        except ValueError:
            print('Please enter between 1 and 99 cents')
            continue
        else:
            return user_input
            break

# Determines the least amount of coins 
# it would take return the selected amount #
def num_coins(cents):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents = cents - coin
            count = count + 1
    return count

if __name__ == '__main__':

    # Prompts users to enter the amount 
    # of change they would like #
    request = input_range('Please enter the amount of cents: ')
    result = num_coins(request)
    print(result)