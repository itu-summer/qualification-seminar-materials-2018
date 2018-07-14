from moby_dick import CHAPTER_1


input_text = CHAPTER_1[0]
# string.strip() removes whitespace from beginning and end of string,
# string.split() splits a string into a list of strings using whitespace
# to find where to split
words = input_text.strip().split()
print("Number of words", len(words))

total_chars = 0  # chars is an abbreviation of characters
for word in words:
    # increase the value of total_chars with the length of each word
    total_chars += len(word)
print("Number of characters", total_chars)
