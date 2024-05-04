course = "PYTHON PROGRAMMING LANGUAGE"

tuitor = "Mark Arthur"

# string concatination
full = course + " " + tuitor

# using format string method to concatinate string
fomat = f"{course} {tuitor}"

user_input = "   my name is   Mark Shija"

# Some of the string method in actions
print(user_input.strip())
print(user_input.find("Shi"))
print(user_input.strip().replace("Mark", "Mosh Hamadan"))
print(course.title())
print(course.lower())
print(course.upper())
print(full)
print(fomat)
print("Shija" in user_input)
print("Shija" not in user_input)
