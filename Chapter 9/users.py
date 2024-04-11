class User:
    """Generic user class"""

    def __init__(self, first_name, last_name):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}, how are you?")

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0