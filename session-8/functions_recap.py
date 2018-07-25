import random
from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES


def get_gender_from_cfg(filename):
    with open(filename) as fp:
        contents = fp.read()
    return contents.strip()


def generate_name(gender):
    # generate a name
    female_name = random.choice(FEMALE_NAMES) + ' ' + random.choice(SURNAMES)
    male_name = random.choice(MALE_NAMES) + ' ' + random.choice(SURNAMES)

    if gender == 'female':
        complete_name = 'Ms. ' + female_name
    elif gender == 'male':
        complete_name = 'Mr. ' + male_name
    else:
        complete_name = 'Cookie Monster'

    return complete_name


def generate_email(complete_name):
    msg_sent = random.choice(['letter', 'postcard', 'present', 'invitation'])

    email_msg = f'''Dear {complete_name},

    Thanks for your {msg_sent}.

    Sorry it's taken me so long to write. I hope you're well.
    Good to see you again last week. Look forward to seeing you soon!


    Best regards,
    Your Computer
    '''
    return email_msg


def main():
    gender = get_gender_from_cfg('gender.cfg')
    my_new_name = generate_name(gender)
    my_email_txt = generate_email(my_new_name)
    print(my_email_txt)
    return my_email_txt


if __name__ == '__main__':
    main()
