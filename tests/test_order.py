from lib.Order import Order

def test_order_total():
    myOrder = Order()
    assert myOrder.grand_total() == 99
    