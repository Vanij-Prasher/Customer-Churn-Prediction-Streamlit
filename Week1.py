# 1. Lower Triangular Pattern
rows1 = 5
for i in range(1, rows1 + 1):
    print("* " * i)

print() 
print() 

# 2. Upper Triangular Pattern
rows2 = 5
for j in range(rows2, 0, -1):
    print("* " * j)

print() 
print() 

# 3. Pyramid Pattern
rows3 = 5
for k in range(1, rows3 + 1):
    print(" " * (rows3 - k) + "* " * k)