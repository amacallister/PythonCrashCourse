class Employee:
    """Simple Employee class"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """
        Adds $5,000 to the annual salary by default
        Also accepts a different raise amount
        """
        self.annual_salary += amount