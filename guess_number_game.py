# for make a random number
from random import randint
# for write colored text in cmd/terminal
from colorama import Fore, Style

number_guess = 1
number_prefix = ''
print('welcom to mahan code \n\n\n')
print(f'press {Fore.RED}<ENTER>{Style.RESET_ALL} to start {Fore.GREEN}game{Style.RESET_ALL}!\n')
input()  # wait for press ENTER

the_number = randint(1, 99)  # choose number btw 1 to 99
print(
    f'I choose a number between 1 to 99 now {Fore.RED}your turn {Style.RESET_ALL} to guess it {Fore.GREEN}:){Style.RESET_ALL}\n')

while True:
    # calculate number_prefix
    if number_guess == 1:
        number_prefix = 'st'
    elif number_guess == 2:
        number_prefix = 'nd'
    elif number_guess == 3:
        number_prefix = 'rd'
    else:
        number_prefix = 'th'
    # get guess number and validation
    user_guess = input(f'{number_guess}{number_prefix} guess: ')
    try:
        user_guess = int(user_guess)
    except:
        continue
    # if number correct brek loop
    if user_guess == the_number:
        break
    number_guess += 1
    # help user
    if the_number > user_guess:
        print(f'{Fore.RED}guess a bigger number{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}guess a smaller number{Style.RESET_ALL}')

# show results
if number_guess < 4:
    print(
        f'Wooooooooow your very {Fore.BLUE}smart!{Style.RESET_ALL} you guess my number in {number_guess} guesses')
elif number_guess < 7:
    print(
        f'Good your {Fore.BLUE}smart!{Style.RESET_ALL} you guess my number in {number_guess} guesses')
else:
    print(f'{Fore.RED}WTF{Style.RESET_ALL} your very {Fore.BLUE}stupid!{Style.RESET_ALL} XD  you guess my number in {number_guess} guesses')
