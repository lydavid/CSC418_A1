import math

def bowtie_f(t):
	t = math.radians(t)
	x = 2 * math.sin(t)
	y = 5 * math.sin(t) * math.cos(t)
	return [x, y]

def get_length(p0, p1):
	return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

perimeter = 0;
for i in range(1, 360):
	perimeter += get_length(bowtie_f(i-1), bowtie_f(i))

perimeter += get_length(bowtie_f(360), bowtie_f(0))
print(perimeter)
