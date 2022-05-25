# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

### NOTE! To run this command successfully with relative paths, navigate to the directory 
### holding your .txt file (or whatever file) to be read in your terminal
### 
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        content = f.read()
    
    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    text_list = text.split(' ')
    
    text_list_copy = text_list[:]

    ### cleanup words
    for i, word in enumerate(text_list_copy):
        ### remove punctuations
        if len(text_list_copy) >= i and '?' in word:
            word_copy = word[:]
            word_copy = word_copy.replace('?', '')
            text_list_copy[i] = word_copy
        if len(text_list_copy) >= i and ',' in word:
            word_copy = word[:]
            word_copy = word_copy.replace(',', '')
            text_list_copy[i] = word_copy
        if len(text_list_copy) >= i and '.' in word:
            word_copy = word[:]
            word_copy = word_copy.replace('.', '')
            text_list_copy[i] = word_copy
        
        ### remove \n and ''.
        if word == '':
            if len(text_list_copy) >= i and ',' in text_list_copy[i+1]:
                text_list_copy[i+1] = text_list_copy[i+1][1:-1]
            else:
                text_list_copy[i+1] = text_list_copy[i+1][1:]
            
            text_list_copy.remove(word)

    text_set = set(text_list_copy)

    word_count_dict = {}
    for word in text_set:
        word_count_dict[word] = 0
        for item in text_list_copy:
            if word == item:
                word_count_dict[word] += 1

    ### Check whether the sum of word occurences match the total number of words ### 
    # counter= 0
    # for i, v in word_count_dict.items():
    #     # print(i, v)
    #     counter += int(v)

    print('Total number of words: ' + str(len(text_list_copy)))
    print('Total number of unique words: ' + str(len(word_count_dict)))
    # print(f"counter: {counter}")
    
    return word_count_dict

if __name__ == '__main__':
    print(count_words())
