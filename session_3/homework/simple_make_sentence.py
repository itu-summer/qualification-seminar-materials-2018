import random


def make_sentence(grammar, start_key):
    # First an empty list to add elements of the sentence to
    words = []
    # Get the definition of how to build this sentence
    sentence_structure = grammar[start_key]
    # Choose a random first word and put it in title case
    first_word_list = grammar[sentence_structure[0]]
    first_word = random.choice(first_word_list)
    words.append(first_word.title())
    # Access each element except the first
    for key in sentence_structure[1:]:
        # Choose a random element of a list
        words.append(random.choice(grammar[key]))
    # We can make a list into a single string by using the string method .join()
    # Call on a string of what you want between each element from the list
    # Use an empty string for no spaces
    sentence = ' '.join(words)
    sentence = sentence + '.'
    return sentence


grammar = {
    '_S': ['_A', '_N', '_V'],
    '_A': ['a', 'the'],
    '_N': ['developer', 'teacher', 'student'],
    '_V': ['learns', 'trains', 'tests', 'is', 'studies', 'asks']
}

if __name__ == 'main':
    print(make_sentence(grammar, '_S'))
