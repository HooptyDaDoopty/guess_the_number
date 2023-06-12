# 1 TODO: Generate random number
# 2 TODO: Prompt user for input
# 3 TODO: Check if user's input can be parsed as a number
# 4 TODO: if not, inform the user and prompt again.
# 5 TODO: if yes ->
# 6 TODO:     check if user's number is less than, equal to, or greater than generated number.
# 7 TODO: if user's number is equal to generated number, tell the user they guessed correctly and ask if they want to play again.
# 8 TODO: if user's number is less than or greater than generated number, tell the user, and ask for input again. 
# (repeat 2-8 until they guess correctly)

from random import randint


def prompt_number(msg:str)->int:
    inp = input(f"{msg}\n")
    
    while not inp.isdigit():
        inp = input(f"{msg}\n")
    
    return int(inp)


def main():
    secret = randint(0, 200)
    user_num = prompt_number("What's your number?")

    while user_num != secret:
        if user_num > secret:
            user_num = prompt_number("Secret number is less, try again.")
        elif user_num < secret:
            user_num = prompt_number("Secret number is greater, try again.")
    
    print("You guessed correctly!")


if __name__ == "__main__":
    main()