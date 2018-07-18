def find_names(text):
    # Returns a list of words with the first letter capitalised from a 
    # text 
    counter = {}
    words = text.split() # returns a list of strings from single string - using whitespace to separate list entries 
    previous_word = '.'
    for word in words: 
        if word == word.title()and word not in ['Mr.', 'Mrs.', 'Mme.', 'Ms.', 'I','"I','Miss','Dr.']:  # if a word is identical in it's original form and it's title form then it must have had the first letter capitalised 
            for char in word:
                if char in '".,!?[]':
                    word = word.replace(char,'')
            if previous_word in ['Mr.', 'Mrs.', 'Mme.', 'Ms.'] or previous_word[-1] != '.': 
                counter.setdefault(word, 0) # if a non-existant key is accessed then it's value is zero - if the key does exist the dictionary behaves as normal 
                counter[word] += 1
            else: 
                pass 
        else: 
            pass 
        previous_word = word 
    return list(counter.keys())


def find_10_most_common_names(text):
    """
    Returns a list of words with the first letter capitalised from a text 
    """
    counter = {}
    for char in text:
        if char in '[],':
            text = text.replace(char,'')
    words = text.split() # returns a list of strings from single string - using whitespace to separate list entries 
    previous_word = '.'
    for word in words: 
        if word == word.title() and word not in ['Mr.', 'Mrs.', 'Mme.', 'Ms.', 'I','"I','Miss',"Dr."]:  # if a word is identical in it's original form and it's title form then it must have had the first letter capitalised 
            if previous_word in ['Mr.', 'Mrs.', 'Mme.', 'Ms.','Miss','Dr.'] or previous_word[-1] not in '!?.': 
                counter.setdefault(word, 0) # if a non-existant key is accessed then it's value is zero - if the key does exist the dictionary behaves as normal 
                counter[word] += 1
            else: 
                pass 
        else: 
            pass 
        previous_word = word 
    output_dic = {}
    for i in range(10):
        max_value = 0 
        max_key = ''
        for key, value in counter.items(): 
            if value > max_value:
                max_value = value
                max_key = key 
        output_dic[max_key] = max_value 
        del counter[max_key]
    return output_dic 


def count_words(text):
    counter = {}
    words = text.split() # returns a list of strings from single string - using whitespace to separate list entries 
    for word in words: 
        counter.setdefault(word, 0)
        counter[word] += 1
    return counter


def find_capped_words(text):
    """
    Returns a list of words with the first letter capitalised from a text 
    """
    counter = {}
    words = text.split() # returns a list of strings from single string - using whitespace to separate list entries 
    for word in words: 
        if word == word.title():        # if a word is identical in it's original form and it's title form then it must have had the first letter capitalised 
            counter.setdefault(word, 0) # if a non-existant key is accessed then it's value is zero - if the key does exist the dictionary behaves as normal 
            counter[word] += 1
        else: 
            pass 
    return list(counter.keys())         # take all the keys from the counter and make them into a list (values ignored)


if __name__ == '__main__':
    import sys
    # Call me from the CLI for example with:
    # his_last_bow.txt | python cli_text_analysis.py 

    file = sys.stdin.read()
    with open(file) as f:
        text = f.read()

    print("The names are: ", find_names(text), "\n")

    print("The most common names are: ", find_10_most_common_names(text), "\n")

    print("most common words are: ", count_words(text), "\n")

    print("Capped words: ", find_capped_words(text), "\n")
