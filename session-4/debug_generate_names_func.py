from random import randint
from us_names import SURNAMES, FEMALE_NAMES


def generate_name(last_index_female_names, last_index_surnames):
    start_index = 0

    female_name_index = randint(start_index, last_index_female_names)
    surname_index = randint(start_index, last_index_surnames)
    print(FEMALE_NAMES[female_name_index] + ' ' + SURNAMES[surname_index])


last_index_surnames = len(SURNAMES) - 1
last_index_female_names = len(FEMALE_NAMES) - 1

generate_name(last_index_female_names, last_index_surnames)
generate_name(last_index_female_names, last_index_surnames)
generate_name(last_index_female_names, last_index_surnames)
generate_name(last_index_female_names, last_index_surnames)
