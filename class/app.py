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
    def __init__(self, food="", walk=""):
        self.food = food
        self.walk = walk

    def __str__(self):
        return f"({self.food}) ({self.walk})"

    def Eat(self):
        print(f"User now is time to eat {self.food} then walk by {self.walk}")

new_user = User("Ugali Maharage", "Own Foot")
Action = new_user.Eat()
print(Action)
