import math

polje = 0
polje_1 = 3
polje_2 = 5
polje_3 = 10
polje_4 = polje_1 + polje_2 + polje_3

while polje < polje_4:
  print(polje)
  if polje == polje_4:
    break
  polje += 1
while polje < polje_4:
  polje += 1
  if polje == polje_4:
    continue
  print(polje)
#
#FUNCTION TEST
def donje_polje():
    if donje_polje == polje_4:
        return True
    else:
        return False
def gornje_polje():
    if gornje_polje == polje_4:
        return False
    else:
        return True
print(donje_polje())
print(gornje_polje())
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
tri_recursion(8)

#LAMBDA TEST
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

#ARRAY TEST
cars = ["Ford", "Volvo", "BMW"]
cars.append("Clio")
for x in cars:
  print(x)

#CLASS TEST
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Ivan", 37)
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("Ivan", 37)
print(p1)

#INHERITED FUNCTIONS
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year): #parent class
    super().__init__(fname, lname) #child class
    self.graduationyear = year
    x = Student("Mike", "Olsen", 2019)
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Person("John", "Doe")
x.printname()

q = 9
c = 2
b = q * c
print(b)
text = "hello"
text1 = text + " " + str(b)
print(text1)
print("Ja sam Andrej i imam" + " " + str(q) + " " + "godina")