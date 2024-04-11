class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print the restaurant info."""
        print(f"{self.restaurant_name.title()} is now serving {self.cuisine_type.title()}!")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Increment the number of customers who've been served."""
        self.number_served += increment