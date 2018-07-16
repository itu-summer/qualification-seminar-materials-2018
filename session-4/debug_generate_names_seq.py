from random import randint
from us_names import SURNAMES, FEMALE_NAMES


last_index_surnames = len(SURNAMES) - 1
last_index_female_names = len(FEMALE_NAMES) - 1
start_index = 0

female_name_index = randint(start_index, last_index_female_names)
surname_index = randint(start_index, last_index_surnames)
print(FEMALE_NAMES[female_name_index] + ' ' + SURNAMES[surname_index])

female_name_index = randint(start_index, last_index_female_names)
surname_index = randint(start_index, last_index_surnames)
print(FEMALE_NAMES[female_name_index] + ' ' + SURNAMES[surname_index])

female_name_index = randint(start_index, last_index_female_names)
surname_index = randint(start_index, last_index_surnames)
print(FEMALE_NAMES[female_name_index] + ' ' + SURNAMES[surname_index])

female_name_index = randint(start_index, last_index_female_names)
surname_index = randint(start_index, last_index_surnames)
print(FEMALE_NAMES[female_name_index] + ' ' + SURNAMES[surname_index])
