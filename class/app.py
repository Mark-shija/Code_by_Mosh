#  A class is a new blueprint of creating a new object
#  An object is an instance of an object
#  Example we can hae
#  class: Human
#  Objects: John, Mark, Grace, Arthur

#  we use paschal naming method we define class in py
class User():
    """ 
    let add a constructor in our class user
    """

    def __init__(self, name=None, food=None, walk=None):
        self.name = name
        self.food = food
        self.walk = walk

    # def __str__(self):
    #     """
    #     Returns a string representation of the User object.
    #     """
    #     return (f"(name={self.name}, food={self.food}, walk={self.walk})")

    def Eat(self):
        return (f"{self.name} now is time to eat {self.food} after eating {self.walk}")

    def Run(self):
        return (f"{self.name} dont walk, just run quickly")


new_user = User("Mark", "Ugali Maharage", "walk")
user2 = User("John", "Pizza", "walk")

Action = new_user.Eat()
Action2 = user2.Eat()
print(Action)
print(Action2)

Run1 = new_user.Run()
Run2 = user2.Run()
print(Run1)
print(Run2)
