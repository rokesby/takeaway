import sys
sys.path.append('/Users/reza/Code/takeaway')
# TODO Why do we need this?


#from lib.menu import Menu
from lib.menu import Menu
from lib.menu_item import MenuItem


def test_menu_creation():

    myMenu = Menu()
    assert isinstance(myMenu, Menu)


def test_add_menu_item():
    
    myMenu = Menu()
    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    myMenu.add(myMenuItem)

    assert myMenu.MenuItems == [myMenuItem]


def test_get_full_menu():

    myMenu = Menu()
    assert myMenu.getFullMenu() == "Today's menu is"

    # myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    # myMenu.add(myMenuItem)

    myMenu = Menu()
    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    myMenu.add(myMenuItem)

    assert myMenu.getFullMenu() == "Today's menu is\nChicken soup, Best chicken soup - £1.99"

    myMenuItem2 = MenuItem('Tuna Sandwich', 'Best sarnie', 7.99)
    myMenu.add(myMenuItem2)

    assert myMenu.getFullMenu() == "Today's menu is\nChicken soup, Best chicken soup - £1.99\nTuna Sandwich, Best sarnie - £7.99"