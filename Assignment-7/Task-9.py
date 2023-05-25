# Task-9

import math

points_list = [(5,3), (2,9), (-2,7), (-3,-4), (0,6), (7,-2)]
distance_list = []

for point in points_list:
    distance_list.append(math.sqrt(point[0] ** 2 + point[1] ** 2))

#Why the fuck do I need to sort this?
#These question hints are weird
for i in range(1, len(distance_list)):
    for j in range(len(distance_list) - i):
        if distance_list[j + 1] < distance_list[j]:
            temp = distance_list[j]
            distance_list[j] = distance_list[j + 1]
            distance_list[j + 1] = temp

            temp_2 = points_list[j]
            points_list[j] = points_list[j+ 1]
            points_list[j + 1] = temp_2

min_distance = distance_list[0]
print("Minimum distance =", min_distance)
print(f"Here the closest point is {points_list[0]} which has distance of {min_distance} from the origin.")
