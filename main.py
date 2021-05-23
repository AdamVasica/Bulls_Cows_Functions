import random

secret_num = []
attempts = 0


def main():
    separator = 80 * '-'
    print('Hi there!')
    print(separator)
    print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
    print(separator)


# Computer generating number
def generate_number():
    for i in range(0, 4):
        num = random.randint(1, 9)
        secret_num.append(num)
    if len(secret_num) != len(set(secret_num)):
        secret_num.clear()
        return generate_number()


# Playing the game + conditions
def game():
    global attempts
    my_number = 0

    while my_number != int(''.join(str(i) for i in secret_num)):
        attempts += 1
        cows = 0
        bulls = 0

        my_number = input('Enter a four digit number:')

        # Checking if the input is correct
        if len(my_number) != 4:
            print('The number must contain 4 digits')
            continue

        if my_number[0] == '0':
            print('The number can not start with 0')
            continue

        if my_number.islower() or my_number.isupper():
            print('Please type only numbers')
            continue

        if len(my_number) != len(set(my_number)):
            print('Number can not contain duplicates')
            continue

        guess = []

        for i in range(4):
            guess.append(int(my_number[i]))

        for x in range(4):
            if guess[x] == secret_num[x]:
                bulls += 1

        for j in range(4):
            if guess[j] in secret_num and guess[j] != secret_num[j]:
                cows += 1

        if bulls == 4:
            print('You won the game in', attempts, 'attempts, congratulations!')
            print(80 * '-')
            break

        print(80 * '-')
        print('Your results:')
        print(cows, "cows")
        print(bulls, 'bulls')
        print(80 * '-')

    else:
        game()


def your_results():
    global attempts

    if attempts <= 5:
        print('You did great!')

    if 6 <= attempts <= 10:
        print('Good results!')

    if attempts >= 11:
        print('Try again, you could do better!')


main()
generate_number()
game()
your_results()
