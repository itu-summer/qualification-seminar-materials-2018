import us_names
import random


# first a little code to make sure that the data looks the way we expect it to
# then some procedural code that solves our problem (we could have just done
# that once instead for both male and female)
# then taking the code from the procedural code and making it into a flexible
# function
# lastly calling the functions and printing out the answers in a few different
# ways

# a quick check to see that things are working
print("No. of female names:", len(us_names.FEMALE_NAMES))
print("No. of male names:", len(us_names.MALE_NAMES))
print("No. of surnames:", len(us_names.SURNAMES))

print()  # print an empty line

# ---Randomly choosing names from lists and putting them together---
# https://docs.python.org/3/library/random.html#functions-for-sequences
# random.choice(seq)
# Return a random element from the non-empty sequence seq. If seq is empty,
# raises IndexError.

print("Female names:")
for i in range(10):
    # we are not using the value i - we are just repeating the task 10 times
    # randomly choosing a string from a list twice and adding a space between
    # the two strings
    female_name = random.choice(us_names.FEMALE_NAMES)
    surname = random.choice(us_names.SURNAMES)
    name = female_name + ' ' + surname
    print(name)

print()  # print another empty line

print("Male names:")
for i in range(10):
    male_name = random.choice(us_names.MALE_NAMES)
    surname = random.choice(us_names.SURNAMES)
    name = male_name + ' ' + surname
    print(name)

print()
