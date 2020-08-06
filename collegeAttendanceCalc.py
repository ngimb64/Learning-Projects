# Number input error handling function #
def number_input(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print('Please enter a number: ')
            continue
        else:
            return user_input
            break

if __name__ == '__main__':

    # Prompts users to enter the amount of credits they 
    # are taking and multiplies that number by 94 #
    creds = number_input('How many credits are you taking? ')
    print()
    cred_cost = creds * 94

    # Prompts the user if they are in or out of state students
    # and calculates the cost based on their decisions #
    location = ''
    while location != 'in-state' and location != 'out-of-state':
        location = input('Are you an in-state or out-of-state student? ')
        print()
        if location != 'in-state' and location != 'out-of-state':
            print('Please select one of the provided options: ')

        if location == 'in-state':
            tuition = 3784
        if location == 'out-of-state':
            tuition = 6604

    # Prompts the user if their living situation will be on
    # or off campus and calculates value based off decision #
    living_sit = ''
    while living_sit != 'on-campus' and living_sit != 'off-campus':
        living_sit = input('Are you living on-campus or off-campus? ')
        print()
        if living_sit != 'on-campus' and living_sit != 'off-campus':
            print('Please select one of the provided options: ')

    # If on-campus living is selected the user is prompted to
    # specify what hall or apartment they live in to calculate cost #
    if living_sit == 'on-campus':
        while living_sit != 'Rancourt Hall' and living_sit != 'Fortin Hall' and \
        living_sit != 'Apartment':
            try:
                campus_spot = input('Do you stay at Rancourt Hall, Fortin Hall, or' \
                ' an Apartment? ')
                print()
                if campus_spot != 'Rancourt Hall' and campus_spot != 'Fortin Hall' \
                and campus_spot != 'Apartment':
                    print('Please select one of the provided options: ')
                else:
                    living_sit = campus_spot

                if campus_spot == 'Rancourt Hall':
                    campus_spot = 9340
                    break
                elif campus_spot == 'Fortin Hall':
                    campus_spot = 8600
                    break
                elif campus_spot == 'Apartment':
                    campus_spot = number_input('What is the monthly rate of your rent? ')
                    campus_spot = campus_spot * 12
                    print('your rent will add up to',campus_spot,'for the whole year')
                    print()
                    break
            except:
                break

    # If off-campus living situation is selected the user is prompted to
    # enter their monthly rent so the cost of the year can be calculated #
    if living_sit != 'on-campus' and living_sit == 'off-campus':
        rent = number_input('What is the monthly rate of your rent?  ')
        rent = rent * 12
        print('your rent will add up to',rent,'for the whole year')
        print()

    # Prompts users to enter the amount annually spent on nooks #
    books = number_input('How much on average would you say you spend on books? ')
    print()
    misc = number_input('Are their any other miscellanious costs to take' \
                        ' into consideration? ')
    print()

    # Calculates total cost for off-campus student #
    if living_sit == 'off-campus':
        total = cred_cost + tuition + rent + books + misc
        print()
        print('Your estimated annual cost is:',total)
        quit()

    # Calculates total cost for on-campus student #
    if campus_spot == 'Rancourt Hall' or 'Fortin Hall' or 'Apartment':
        total = cred_cost + tuition + campus_spot + books + misc
        print()
        print('Your estimated annual cost is:',total)