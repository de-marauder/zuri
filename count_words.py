def count_words(text):
    textList = text.split(' ')
    return len(textList)



if __name__ == "__main__":
    print(count_words("Enter some text"))