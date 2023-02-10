import math
G = 6.674 * (10 ** -11)
m1 = float(input("Enter first mass: " ))
m2 = float(input("Enter second mass: "))
F = float(input("Enter a force: "))
distance = (G*m1*m2) /(F)
import math
result = math.sqrt(distance)
print("the distance between the two objects is ")
print(result)