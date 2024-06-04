class MenuItem():
    
    def __init__(self, name, desc, price):
        self.name = name
        self.description = desc
        self.price = price

    def getInformation (self):
        return (self.name +", " + self.description + " - £" + str(self.price))
    


    # myMenuItem = MenuItem('Chicken soup', 'Best chicken soup', 1.99)
    # result = myMenuItem.getInformation()
    # assert result == 'Chicken soup, Best chicken soup - £1.99'    