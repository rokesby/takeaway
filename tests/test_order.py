import sys
sys.path.append('/Users/reza/Code/takeaway')

from lib.Order import Order
from lib.menu_item import MenuItem


def test_create_order():
    myOrder = Order('Me@Mail.com','Me')
    assert isinstance(myOrder, Order)

# Add menu items to the order

def test_add_menu_item_to_order():

    myOrder = Order('Me@Mail.com','Me')
    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    
    myOrder.add(myMenuItem)

    assert myOrder.MenuItems == [myMenuItem]


    myMenuItem2 = MenuItem('Pea soup', 'Best pea soup', 2.99)
    myOrder.add(myMenuItem2)

    assert myOrder.MenuItems == [myMenuItem, myMenuItem2]


# Store customer details.
def test_store_details():
    myOrder = Order('Me@Mail.com','Me')
    assert myOrder.email == 'Me@Mail.com' and myOrder.name == 'Me'
# View order details
def test_order_details():
    myOrder = Order('Me@Mail.com','Me')
    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    myOrder.add(myMenuItem)
    myMenuItem2 = MenuItem('Pea soup', 'Best pea soup', 2.99)
    myOrder.add(myMenuItem2)
    assert myOrder.view_order() == 'Chicken soup - £1.99\nPea soup - £2.99\nTotal - £4.98'
# Get total cost

#Place order
def test_place_order():
    myOrder = Order('Me@Mail.com','Me')
    myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    myOrder.add(myMenuItem)
    myMenuItem2 = MenuItem('Pea soup', 'Best pea soup', 2.99)
    myOrder.add(myMenuItem2)
    assert myOrder.place_order() == 'Thanks Me, your order will arrive by 21:00 - a confirmation email has been sent to Me@Mail.com'