while True:
    n = input()
    if n == '#':
        break

    count_vowel = (n.count('a') + n.count('e') + n.count('i') +
                   n.count('o') + n.count('u') +
                   n.count('A') + n.count('E') + n.count('I') +
                   n.count('O') + n.count('U'))
    print(count_vowel)