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


