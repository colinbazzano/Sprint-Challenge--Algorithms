'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.

count the words
base case for if the word is less than 2 letters, obviously cannot contain th
if it starts with th

'''


def count_th(word):
    word_count = 0
    if len(word) < 2:
        return word_count
    elif word[:2] == "th":
        word_count = 1 + count_th(word[2:])
    else:
        word_count = count_th(word[1:])
    return word_count


# testing for my own sanity
word = "th I went through the drive thru"
print(count_th(word))
