def guess_color(real, guess):
    half = 0
    all = 0

    if not isinstance(guess, list):
        print("please enter a list! ")
    elif len(guess) != len(real):
        print("length not equal!")
    else:
        for i in range(0, len(guess)):
            if guess[i] == real[i]:
                all += 1
            if guess[i] in real and guess[i] != real[i]:
                half += 1

    return all, half

if __name__=="__main__":
    real = ["red", "blue", "yellow", "green"]
    guess = eval(input("please input the color as a list"))
    all, half = guess_color(real, guess)
    print(" all: ", all, "\n", "half: ", half)
