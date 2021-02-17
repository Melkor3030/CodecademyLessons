#Types
print(type(5))

my_dict = {}

print(type(my_dict))

my_list = []

print(type(my_list))

#Class
class Facade:
  pass

#Instantiation
facade_1 = Facade()

#Object-Oriented Programming
facade_1_type = type(facade_1)

print(facade_1_type)

#Class Variables
class Grade:
  minimum_passing = 65

#Methods
class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#Methods with Arguments
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius **2

circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

#Constructors
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter:{diameter}".format(diameter=diameter))

teaching_table = Circle(36)

#Instance Variables
class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#Attribute Functions
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else: 
    print(str(type(element)) + " does not have the count attribute :(")

#Self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#Everything is an object
dir(5)

def this_function_is_an_object(art, num_pens):
  return "If you are doing a {} project you will need {} pens".format(art, num_pens)

print(dir(this_function_is_an_object))

#String Representation
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius {radius}".format(radius = self.radius)
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza,teaching_table,round_room)

#Review
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grades):
    if type(grades) is Grade:
      self.grades.append(grades)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))


