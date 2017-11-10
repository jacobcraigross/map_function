import math
def area(r):
    # Area of a circle with radius r.
    return math.pi * (r ** 2)

radii = [4, 55, 7, 7.03, 12, 0.3, 1.38837736]

# Method 1
areas = []
for r in radii:
    a = area(r)
    areas.append(a)
print areas

# Method 2 (using map function)
map(area, radii)
results = list(map(area, radii))
print results
