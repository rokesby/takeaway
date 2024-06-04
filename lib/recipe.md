# {{PROBLEM}} Todo Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE


def get_menu():
    
    Parameters: 
        none

    Returns: (a list of strings detailing the item and the cost per unit, and maybe the availability)
        a list of strings
        an empty list of no active tasks exist


    Side effects: 
        none
    
```

def order_items(Order items from the menu):
    
    Parameters: 
        task_description : A list of items that constitute the order. repeated entries indicate the order number e.g. [chicken, chicken] means two portions of the chicken dish

    Returns:
        none

    Side effects: 
        Do not do anything, or maybe raise an exception if the specified task does not exist
    """
    pass # Test-driving means _not_ writing any code here yet.
```


def get_order_total():
    """
    Parameters:
        None

    Returns: 
        Total - a float indicating the total cost of the meal so the customer can decide on whether to order or not?

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```


## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Prerequisite - populate the menu as a one off activity
Confirm that the menu is empty
Populate the menu and confirm it is not empty

"""
get_menu() => []

"""
Add 1 menu item and then retrieve the menu
Returns a list of 1 menu item which includes a description of the dish and it's price

"""
add_to_menu("specific dish")
get_menu() => ["specific dish"]

"""
Add 2 menu items and then retrieve the menu
Returns a list of 2 elements


"""

get_order_total() => Floating number


"""
Empty - Confirm that an empty order has no cost
Populated - Confirm the order cost is correct for a predefined order

"""

get_order_confirmation() => Email received by customer

"""
Confirm that an email has been sent to the customer with a delivery time slot

"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
