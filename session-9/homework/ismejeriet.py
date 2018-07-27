from random import choice
from itu_queue import Queue


class Customer():

    # TODO: Implement me!
    pass


class ShopAssistant():

    # TODO: Implement me!
    pass


def get_queue_length_from_file():
    # TODO: Implement me!
    pass


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
