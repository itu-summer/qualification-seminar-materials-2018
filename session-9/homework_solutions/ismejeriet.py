from time import sleep
from itu_queue import Queue
from random import choice, randint, choices
from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES


class Customer():

    def __init__(self, gender='female'):
        if gender == 'female':
            self.name = choice(FEMALE_NAMES) + ' ' + choice(SURNAMES)
        elif gender == 'male':
            self.name = choice(MALE_NAMES) + ' ' + choice(SURNAMES)
        else:
            self.name = 'Cookie Monster'

    def say_name(self):
        return self.name

    def choose_icecream(self):
        icecream = ['Strawberry', 'Chocolate', 'Vanilla', 'Sea Buckthorn',
                    'Lime', 'Mango']
        number_of_balls = randint(1, 5)
        return choices(icecream, k=number_of_balls)


class ShopAssistant():

    def __init__(self, speed):
        self.serving_speed = speed
        gender = choice(['female', 'male'])
        if gender == 'female':
            self.name = choice(FEMALE_NAMES)
        elif gender == 'male':
            self.name = choice(MALE_NAMES)
        self.name = self.name + ' ' + choice(SURNAMES)
        self.busy = False

    def serve_icecream_to(self, customer):
        self.busy = True
        which_icecream = customer.choose_icecream()
        customer_name = customer.say_name()
        time_for_serving = len(which_icecream) * self.serving_speed
        print(f'I {self.name}, serve {which_icecream} to {customer_name}.')
        print(f'   --> It will take {time_for_serving} seconds.')
        sleep(time_for_serving)
        self.busy = False


def get_queue_length_from_file():
    with open('config.cfg') as fp:
        for line in fp:
            return int(line)


def run_simulation():

    ismejeriet = Queue()
    amount_of_customers = get_queue_length_from_file()
    # Let's say we have 100 customers queueing
    for customer in range(amount_of_customers):
        customer_gender = choice(['female', 'male', 'unknown'])
        new_customer = Customer(customer_gender)
        ismejeriet.enqueue(new_customer)

    shop_assistant = ShopAssistant(2)

    while not ismejeriet.is_empty():
        customer = ismejeriet.dequeue()
        shop_assistant.serve_icecream_to(customer)
        print(f'{ismejeriet.size()} customers left in queue')


if __name__ == '__main__':
    run_simulation()
