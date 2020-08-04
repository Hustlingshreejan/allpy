game_num=43
total_guess=5
guess=1

while guess<=5:
    user=int(input("Enter the number for a guess: "))
    if user < game_num:
        print("Your number is smaller")
        print("You have",total_guess-guess,"guesses left\n")
        guess += 1
    elif user > game_num:
        print("Your number is greater")
        print("You have", total_guess - guess, "guesses left\n")
        guess += 1
    else:
        print("You have guessed the correct number")
        print("Congrats you have guessed the right in",guess,"attempt")
        print("You have", total_guess - guess, "guesses left")
        break


if guess >5:
    print("Number of guesses Game over")
