'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Base case: if len(word) <= 1 return 0 because it cannot contain th if it is only 1 letter
    # else, we want to check if the first two letters are th, then check for the rest of the word
    word_count = 0
    if len(word) <= 1:
        return word_count  # no point in still looking, there's not enough letters
    elif word[:2] == "th":
        word_count = 1 + count_th(word[2:])
    else:
        word_count = count_th(word[1:])
    return word_count
