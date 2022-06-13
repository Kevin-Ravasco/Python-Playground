

def palindrome(word):
    if word == word[::-1]:
        return print(-1)

    words = word
    for char in words:
        if words.count(char) >= 2:
            words = words.replace(char, '')

    return print(len(words))


test = ['aaab', 'baa', 'aaa']

# for t in test:
#     palindrome(t)

palindrome(test[2])
