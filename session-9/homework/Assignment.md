# Assignment 9


## Ismejeriet Simulator

Let's write a simulation of Ismejeriet, the ice cream shop opposite ITU.

The purpose of this assignment is to get more practice in writing classes and methods, i.e, object-oriented programs.

  * Implement the missing parts of the module `ismejeriet.py`.
  * In it define two classes, one called `Customer` and the other one called `ShopAssistant`.

### The `Customer` Class

  * A `Customer` shall have three methods. A constructor, i.e.,  `__init__`, one to tell the customer's name `say_name`, and one for choosing ice cream `choose_icecream`.
  * Additionally, it has a property called `name`.
  * Let the constructor receive an argument `gender`, so that you can create customer objects via `Customer('female')` or via `Customer('male')`.
    - Depending on the given `gender` argument the `name` property is set to a female or to a male name.
    - In case `gender` is neither `'female'` nor `'male'`, the `name` of the `Customer` object shall be set to `'Cookie Monster'`.
    - Use the names of `us_names.py` to create random names.
  * The method `say_name` shall only return the `name` of the `Customer` object and do nothing else. 
  * The method `choose_icecream` shall return a list of which ice cream the customer wants to order.
    - The customer can choose from the following:
    ```python
    ['Strawberry', 'Chocolate', 'Vanilla', 'Sea Buckthorn', 'Lime', 'Mango']
    ```
    - A customer can choose in between 1 to 5 balls of ice cream.

## The `ShopAssistant` Class
  * A `ShopAssistant` shall have two methods. A constructor, i.e.,  `__init__`, and another one to serve ice cream `serve_icecream_to`.
  * Additionally, the `ShopAssistant` class has a properties called `serving_speed`, `name`, and `busy`.
    - The default value for `busy` is `False`
    - The `name` can be any string of your liking
  * Let the constructor receive an argument `speed`, which provides the value for the property `serving_speed` at object creation time. That is, you can create a `ShopAssistant` object via `ShopAssistant(2)` where the `serving_speed` is set to 2 then.
  * The method `serve_icecream_to` shall receive a `Customer` object as argument. 
    - The `Customer` object shall be used within this method to ask it for the name and to let it choose ice cream via `customer.say_name()` and `customer.choose_icecream()` respectively.
    - The property `busy` shall be set to true for the runtime of this method.
    - The method takes some time. You can simulate serving time with the help of the `sleep` function from the `time` module.
    - The time the method takes shall depend on how many ice cream has to be served and the serving speed of the shop assistant.

## Reading a value from a configuration file

Implement the function `get_queue_length_from_file` so that it reads the amount of customers in the queue from a corresponding configuration file.


## Running the simulation

Running your implementation of the simulation shall produce output similar to the following.

```bash
$ python ismejeriet.py
I Devorah Nute, serve ['Mango', 'Lime', 'Vanilla', 'Chocolate'] to Cookie Monster.
   --> It will take 8 seconds.
9 customers left in queue
I Devorah Nute, serve ['Sea Buckthorn', 'Vanilla', 'Lime'] to Alline Elizondo.
   --> It will take 6 seconds.
8 customers left in queue
I Devorah Nute, serve ['Chocolate'] to Shirlene Kundrick.
   --> It will take 2 seconds.
7 customers left in queue
I Devorah Nute, serve ['Sea Buckthorn', 'Vanilla', 'Strawberry', 'Vanilla', 'Chocolate'] to Cookie Monster.
   --> It will take 10 seconds.
6 customers left in queue
I Devorah Nute, serve ['Vanilla', 'Strawberry'] to Cookie Monster.
   --> It will take 4 seconds.
5 customers left in queue
I Devorah Nute, serve ['Lime', 'Vanilla', 'Mango', 'Sea Buckthorn'] to Juliette Voyles.
   --> It will take 8 seconds.
4 customers left in queue
I Devorah Nute, serve ['Lime', 'Chocolate'] to Elmer Caivano.
   --> It will take 4 seconds.
3 customers left in queue
I Devorah Nute, serve ['Vanilla', 'Lime'] to Cookie Monster.
   --> It will take 4 seconds.
2 customers left in queue
I Devorah Nute, serve ['Lime', 'Mango'] to Taylor Denby.
   --> It will take 4 seconds.
1 customers left in queue
I Devorah Nute, serve ['Lime', 'Chocolate', 'Sea Buckthorn', 'Vanilla'] to Cookie Monster.
   --> It will take 8 seconds.
0 customers left in queue
```















## Challenge

This assignment is optional and for the adventurous.

Read the article on patterns of graph implementation in Python https://www.python.org/doc/essays/graphs/.

The article gives an example for another algorithm for finding a path between two nodes. It is a depth-first search algorithm. Try to adapt the given algorithm to work with our `Graph` ADT.