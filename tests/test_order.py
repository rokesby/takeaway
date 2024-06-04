import sys
sys.path.append('/Users/reza/Code/takeaway')

from lib.Order import Order

def test_order_total():
    myOrder = Order()
    result = myOrder.grand_total()
    
    assert result == 99
    