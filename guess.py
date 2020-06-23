import random
def guess_color(real, guess):
    if isinstance(guess, list) and len(guess) == len(real):
        return valid_guess(real, guess)
    else:
        return -1
        print("invalid input")


def valid_guess(real, guess):
    half = 0
    all = 0
    for i in range(0, len(guess)):
        if guess[i] == real[i]:
            all += 1
        if guess[i] in real and guess[i] != real[i]:
            half += 1
    return all, half


if __name__ == '__main__':
    real_set = ['red', 'yellow', 'blue', 'green', 'white', 'pink']
    real = random.sample(real_set, 4)
    for i in range(0, 7):
        guess_list = list(map(str, input("\nPlease input 4 colors in order, separated by spaces").strip().split()))
        all, half = guess_color(real, guess_list)
        print("all: ", all, "\nhalf: ", half)
        if all == 4:
            print("Congratulations!")
            break
        else:
            print(6-i, "chances left")
    print(real)
