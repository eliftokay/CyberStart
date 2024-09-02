import math

points= [(x,y), (a,b)]
def euclideanDistance(point1, point2):
    (x1, y1) = point1
    (x2, y2) = point2
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return distance
distances = []
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))
distances.sort()
min_distance=distances[0]
max_distance=distances[-1]