import math

arg = [[0, 0], [3, 9], [12, 0]]
ax = arg[0][0]
bx = arg[1][0]
cx = arg[2][0]
ay = arg[0][1]
by = arg[1][1]
cy = arg[2][1]

#a = math.sqrt((cx - bx) ** 2 + (cy - by) ** 2)
#b = math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
#c = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)

#x = (-(a ** 2) + (b ** 2) + (3 * c **2)) / 6 * c
#y = (((a + b - c) * (a - b + c) * (-a + b + c) * (a + b + c)) ** 0.5 / 6 * c)

x = (ax + bx + cx) / 3
y = (ay + by + cy) / 3
print([x, y])