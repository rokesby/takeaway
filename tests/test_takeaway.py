# import sys
# sys.path.append('/Users/reza/Code/takeaway')

from lib.menu_item import *


def test_create_menu_item():

    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    assert isinstance(myMenuItem, MenuItem)

    # Check all properties - item_name, item_description, item_price

    assert myMenuItem.price == 1.99
    assert myMenuItem.description == 'Best chicken soup'
    assert myMenuItem.name == 'Chicken soup'



def test_format_menu_item_for_menu():

    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    result = myMenuItem.getInformation()
    assert result == 'Chicken soup, Best chicken soup - £1.99'    