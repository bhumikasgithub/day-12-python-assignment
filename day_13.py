"""#1
import math

C = 50
H = 30

input_str = input("Enter comma-separated D values: ")

d_values = [int(d) for d in input_str.split(',')]

results = []
for D in d_values:
    Q = math.sqrt((2 * C * D) / H) 
    results.append(round(Q))  

print(",".join(str(q) for q in results))"""


#2
x, y = map(int, input("Enter two numbers X,Y (e.g., 3,5): ").split(','))

result = [[i * j for j in range(y)] for i in range(x)]

print(result)

