from lib.menu_item import MenuItem

class Menu():

    def __init__(self):
        self.MenuItems = []

    def add(self, newMenuItem):
        self.MenuItems.append(newMenuItem)

    def getFullMenu(self):
        
        output_string = "Today's menu is"

        for item in self.MenuItems:
            output_string += '\n' + item.getInformation()

        return output_string