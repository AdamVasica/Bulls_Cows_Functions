import random

secret_num = []
attempts = 0

def main():
    separator = 80 * '-'
    print('Hi there!')
    print(separator)
    print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
    print(separator)

#Computer generating number
def generate_number():
    for i in range(0,4):
        num = random.randint(1,9)
        secret_num.append(num)
    if len(secret_num) != len(set(secret_num)):
        secret_num.clear()
        return generate_number()


#Playing the game + conditions
def game():
    global attempts
    my_number = 0

    while my_number != int(''.join(str(i) for i in secret_num)):
        attempts += 1
        cows = 0
        bulls = 0
        print(secret_num)
        my_number = input('Enter a four digit number:')



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

        print(cows, "cows")
        print(bulls, 'bulls')

        if bulls == 4:
            print('You won the game in', attempts, 'attempts, congratulations!')
        else:
            game()



main()
generate_number()
game()
print(secret_num)