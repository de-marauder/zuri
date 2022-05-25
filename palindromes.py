def find_palindrome(word):
    # [assignment] Add your code here

    return word.lower() == word[::-1].lower()


print(find_palindrome('Racecar'))
print(find_palindrome('hello'))