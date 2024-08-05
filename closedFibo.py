import math

n = int(input("Enter fibonacci N: "))

f = (1/math.sqrt(5)) * ((1 + math.sqrt(5))/2)**n - (1/math.sqrt(5)) * ((1-math.sqrt(5))/2)**n

print(f)
