#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pprint
import numpy as np
from math import sqrt
from random import randint

POINT = tuple[float, float, float]

def distance(p1: POINT, p2: POINT) -> float:
    
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def k_means(points: list[POINT], centers: list[POINT]) -> list[dict]:
    result = [
        {
            "center": center,
            "points": [],
        }
        for center in centers
    ]
    for point in points:
        index, minimum = 0, distance(point, centers[0])
        for i, center in enumerate(centers[1:], start=1):
            d = distance(point, center)
            if d < minimum:
                index, minimum = i, d
        result[index]["points"].append(point)
    return result

file_path = "points.txt"
points = []
with open(file_path, 'r') as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) == 3:
            try:
                x, y, z = float(data[0]), float(data[1]), float(data[2])
                points.append((x, y, z))
            except ValueError:
                print("Invalid data:", line)

points = np.array(points)
points = points[~np.isnan(points).any(axis=1)]
points = points[~np.isinf(points).any(axis=1)]

K = int(input("Please enter the number of clusters (K): "))

centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(K)]

while True:
    clusters = k_means(points, centers)
    new_centers = []
    for cluster in clusters:
        if cluster["points"]:
            x, y, z = zip(*cluster["points"])
            new_centers.append(
                (
                    sum(x) / len(x),
                    sum(y) / len(y),
                    sum(z) / len(z),
                )
            )
    if new_centers == centers:
        break
    centers = new_centers

pprint.pprint(clusters)


# In[ ]:




