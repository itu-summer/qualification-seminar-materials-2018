import random
import us_names


def generate_names(gender, number):
    """Function creating a list of names, which are randomly created out
    of names from the US census 1990.
    
    Arguments:
        gender {str} -- the gender of the name. Can be 'female' or 'male'
        number {int} -- amount of names in the returned list
    
    Returns:
        list -- A list of strings woth either female or male US names.
    """   
    all_names = []
    if gender == 'female':
        names = us_names.FEMALE_NAMES
    elif gender == 'male':
        names = us_names.MALE_NAMES
    else:
        print("Error: Gender should be either 'female' or 'male'")
    for _ in range(number):
        name = random.choice(names)
        surname = random.choice(us_names.SURNAMES)
        fullname = name + ' ' + surname
        all_names.append(fullname)
    return all_names