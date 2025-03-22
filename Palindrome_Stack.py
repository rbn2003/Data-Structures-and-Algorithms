def palindrome_word(word):
    stack = []

    for char in word:
        stack.append(char)

    reversed_word = ""

    while stack:
        reversed_word += stack.pop()

    return word == reversed_word

print(palindrome_word("radar"))
print(palindrome_word("first"))

