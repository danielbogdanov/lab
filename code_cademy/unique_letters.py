letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def uniq(word):
    counter = 0
    for letter in letters:
        if word.count(letter) == 1:
            counter += 1
    return counter


print(uniq('mississippi'))
