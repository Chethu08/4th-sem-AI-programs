num=49

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 100")

while True:
    g=int(input("Guess the number (1-100): "))

    if g==num:
        print("Congratulations! You guessed correctly!")
        break
    elif g<num:
        print("Too low! Try again")
    else:
        print("Too high! Try again")