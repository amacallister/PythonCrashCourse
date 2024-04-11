from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Generic ice cream stand class that inherits from the Restaurant class"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Initialize variables of the parent Restaurant class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.cuisine_type = 'Ice Cream'
        self.flavors = flavors

    def display_flavors(self):
        """Display ice cream flavors."""
        print("Here is a list of ice cream flavors we offer: ")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")
    