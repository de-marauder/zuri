# Check if a word is a anagram
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagram(word1, word2):
    # [assignment] Add your code here
   
    return sorted(word1.lower()) == sorted(word2.lower())


print(find_anagram('Race', 'care'))
print(find_anagram('hello', 'hollo'))
