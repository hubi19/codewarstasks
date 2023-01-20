def solution(text, ending):

    len_ending = len(ending)

    len_text = len(text)


    if text[len_text-len_ending::] == ending:

        return True
    else:

        return False

print(solution('miut', 'ut'))