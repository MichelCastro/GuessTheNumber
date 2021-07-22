from random import randint


def number_msg(rand_num, num):
    if num == rand_num:
        return f'You got it!! The number is {rand_num}'
    if rand_num - 5 < num < rand_num + 5:
        return "You're so Close!"
    else:
        return "You're far away!"


def again(chose):
    if chose == 'y':
        print('\n'*20)
        main()
    else:
        pass


def main():
    lives = 5
    r_num = randint(0, 20)
    for live in range(lives, 0, -1):
        number = int(input('Digit an integer number: '))
        print(number_msg(r_num, number))
        if number == r_num:
            break
        if live == 1:
            print(f'You have {live - 1} lives!\nGAME OVER!')
            break
        print(f'You have {live - 1} lives!')
    chose = input('Do you want to play again? (y/or any key to NO)')
    again(chose)


print('Welcome to the Guess the Number!!\n\n'
      'Description:\n\n'
      'The program will be generated a number 0 to 20, and you needs to guess the number!\n'
      'You have 5 lives, good lucky!!\n\n', '#' * 20)

main()

print('Thank you!')