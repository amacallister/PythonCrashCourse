from users import User

class Privileges():
    """Initialize attributes to describe a privilege."""

    def __init__(self):
        """Initialize attributes to describe a privilege."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """List the administrator's set of privileges."""
        print("Here is a list of privileges for this user:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Generic admin class that inherits from the User class"""

    def __init__(self, first_name, last_name):
        """
        Initialize variables of the parent User class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()