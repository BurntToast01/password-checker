# Load the variables I will be using for the program
special_chr = "!" " ""#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
num_counter = 0
special_chr_counter = 0
letter_count = 0


def main():
    print('\nYour password must be 6 digits or letter long, it must include a number, letter, and a special character '
          'such as eg: ')
    print(special_chr)
    print('Please enter your password: ')
    # in a while True block prompt the user for an input that is longer than 6 in length
    while True:
        a = input()
        if len(a) < 6:
            print(
                '\nYour password must be 7 digits or letter long, it must include a number, letter, and a special '
                'character such as eg:.')
            print(f'what you typed was only {len(a)} long. Try again\n')
            continue
        else:
            if len(a) >= 6:
                # Once the user input has a length of 7 or higher we can break and call the next function
                # we're passing the user input and the variables from the top as arguments
                checking(a, num_counter, special_chr_counter, letter_count)
                break


def checking(a, b, c, d):
    # load arguments as variables
    b = b  # this is num_counter
    c = c  # this is special_chr_counter
    d = d  # this is letter_count
    # in a while true block we check every character from the input and start to add into our variables
    # we will add into our variables based on if it's a number, digit, or a special character with +=1
    while True:
        if len(a) >= 6:
            for x in a:  # for every character in the user input
                if x.isdigit() or x.isnumeric():  # if it's a digit or numerical add to b, which is num_counter
                    b += 1
                if x.isalpha():  # if it's alphabet letter add to d, which is letter_count
                    d += 1
                for y in special_chr: # in a for loop we compare every character in the special character things in user
                    # input to see if there is a special character. if there is a special character, we add one to it.
                    if x in y:
                        c += 1
            # after doing a count of each character we check to make sure that none of the counters are 0
            # if any of the counters are zero we call the main function and break out of the current function
            if b <= 0:
                if c<=0:
                    # this block will execute if there is not a number or a special character in the input string
                    print('you dont have any numbers or special characters')
                    main()
                    break
                if d<=0:
                    if c<=0:
                        print('you do not have any numbers or alphabetical letters')
                        main()
                        break
                    # if the conditional check finds a number and a special character this block will execute
                    print('you dont have any letters or numbers')
                    main()
                    break
                print('you do not have any numbers')
                main()
                break
            if c <= 0:
                if d<=0:
                    # if there are no letters or special character this block will execute
                    print('you dont have any letters or special characters')
                    main()
                    break
                print('you do not have any special characters')
                main()
                break
            if d <= 0:

                # if there are numbers and special characters this will execute
                print('you dont have a letter')
                main()
                break
            # if all the counters are greater than 0 we will call out printing function, passing our counters are
            # arguments
            if b > 0:
                if c > 0:
                    if d > 0:
                        printing(b, c, d)
        break


def printing(a, b, c):
    a = a # this is num_counter
    b = b # this is special_chr_counter
    c = c # this is letter_count
    print(f'number count is {a}')
    print(f'special character count is {b}')
    print(f'you character count is {c}')
    print('you have a strong password')


if __name__ == '__main__':
    main()
