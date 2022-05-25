# Check if a word is a palindrome
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_palindrome(word):
    # [assignment] Add your code here
    if word.lower() == word[::-1].lower():
        return True

    return False


print(find_palindrome('Racecar'))
print(find_palindrome('hello'))
