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