# Implement Students room using OOP:

# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")

# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def output(self):
        return "name: ",self.name, "age: ",str(self.age), "major: ", self.major

st1 = Student("Steven Schultz", 23, "English").output()
st2 = Student("Jonathan Rosenberg", 24, "Biology").output()
st3 = Student("Penelope Meramveliotakis", 21, "Physics").output()

print(" ".join(st1))
print(" ".join(st2))
print(" ".join(st3))


