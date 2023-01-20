def is_isogram(string):

    lowercase = string.lower()

    if len(lowercase) == len(set(lowercase)):

        return True
    else:

        return False