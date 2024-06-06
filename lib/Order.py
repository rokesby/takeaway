from lib.mailgun import *
from datetime import datetime

class Order():

    def grand_total(self):
        return 99
    
    def __init__(self, email, name):
        self.MenuItems = []
        self.email = email
        self.name = name

    def add(self, newMenuItem):
        self.MenuItems.append(newMenuItem)
    
    def view_order(self):
        Order = ''
        Cost = 0
        for item in self.MenuItems:
            Order += item.name + ' - £' + str(item.price) + '\n'
            Cost += item.price
        Order += 'Total - £' + str(Cost)
        return Order

    def place_order(self):
        current_date_and_time = datetime.now()
        mailer = SendMailer()
        mailer.send_single_email("Reza <rezajugon@icloud.com>", "Takeaway order confirmed!", "Your order will arrive by 21:00 - now" + str(current_date_and_time))
        return  f'Thanks {self.name}, your order will arrive by 21:00 - a confirmation email has been sent to {self.email}'