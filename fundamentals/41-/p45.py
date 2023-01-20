def get_count(sentence):

    vowels = ['a', 'e', 'i', 'o', 'u']

    sum = 0

    for letter in sentence:
        if letter in vowels:
            sum += 1
    return sum