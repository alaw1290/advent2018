# day 6 challenge
import time

def m_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) # return manhattan distance

def next_point_set(center_p, delta_x, delta_y):
    points = []
    bound_x_min, bound_x_max = center_p[0] - delta_x, center_p[0] + delta_x 
    bound_y_min, bound_y_max = center_p[1] - delta_y, center_p[1] + delta_y
    for y in range(bound_y_min, bound_y_max+1):
        points.append((bound_x_min,y))
        points.append((bound_x_max,y))
    for x in range(bound_x_min+1, bound_x_max):
        points.append((x,bound_y_min))
        points.append((x,bound_y_max))
    return points

points_label_dict = {}
points_distance_dict = {}

def find_closest_center(point, centers_dict):
    if point in points_label_dict:
        return points_label_dict[point]
    else:
        distances = sorted([(m_distance(centers_dict[c], point), c) for c in centers_dict], key=lambda x: x[0])
        points_distance_dict[point] = sum([i[0] for i in distances])
        if distances[0][0] == distances[1][0]: # more than 1 closest center
            points_label_dict[point] = None
            return None
        else:
            points_label_dict[point] = distances[0][1]
            return distances[0][1] # only one closest center

def get_distances_for(points, centers_dict):
    distances = []
    for point in points:
        if point in points_label_dict:
            distances.append(points_distance_dict[point])
        else:
            d = sum([m_distance(centers_dict[c], point) for c in centers_dict])
            points_distance_dict[point] = d
            distances.append(d)
    return distances

def get_labels_for(points, centers_dict):
    labels = []
    for point in points:
        labels.append(find_closest_center(point, centers_dict))
    return labels

def calc_center_area(center, centers_dict):
    delta_x = 0
    delta_y = 0
    total_area = 1
    center_p = centers_dict[center]
    while True:
        delta_x += 1
        delta_y += 1
        points = next_point_set(center_p, delta_x, delta_y)
        labels = get_labels_for(points, centers_dict)
        area = len([i for i in labels if i == center])
        if area == 0:
            break
        else:
            total_area += area
    return total_area

def calc_area_under_cutoff(center_p, cutoff, centers_dict):
    delta_x = 0
    delta_y = 0
    total_area = 1
    while True:
        delta_x += 1
        delta_y += 1
        points = next_point_set(center_p, delta_x, delta_y)
        distances = get_distances_for(points, centers_dict)
        # print(distances)
        area = len([i for i in distances if i < cutoff])
        if area == 0:
            break
        else:
            total_area += area
    return total_area

def main():
    start = time.time()
    centers_dict = {}
    x_coords = []
    y_coords = []
    with open('coordinates.txt', 'r') as file:
        center_id = 1
        for line in file:
            linex,liney = line.strip().split(', ')
            linex,liney = (int(linex), int(liney))
            centers_dict[center_id] = (linex,liney)
            x_coords.append(linex)
            y_coords.append(liney)
            center_id += 1

    bound_x_min, bound_x_max = min(x_coords), max(x_coords)
    bound_y_min, bound_y_max = min(y_coords), max(y_coords)
    # part 1
    # step 1: get all edge centers and remove them from consideration
    ignored_centers = set()
    for y in range(bound_y_min, bound_y_max+1):
        ignored_centers.add(find_closest_center((bound_x_min,y), centers_dict))
        ignored_centers.add(find_closest_center((bound_x_max,y), centers_dict))
    for x in range(bound_x_min+1, bound_x_max):
        ignored_centers.add(find_closest_center((x,bound_y_min), centers_dict))
        ignored_centers.add(find_closest_center((x,bound_y_max), centers_dict))

    # step 2: compute area of each center in consideration
    considered_centers = [c for c in centers_dict if c not in ignored_centers]
    center_areas = {c:0 for c in considered_centers}
    for center in considered_centers:
        center_areas[center] = calc_center_area(center,centers_dict)
    print(f"max finite area: {max([(center_areas[i], i) for i in center_areas])}")

    # part 2
    # start from midpoint and spiral out
    start_x = (bound_x_min + bound_x_max) // 2
    start_y = (bound_y_min + bound_y_max) // 2
    print(f"max area under cutoff {calc_area_under_cutoff((start_x,start_y), 10000, centers_dict)}")

    print(time.time() - start)






if __name__ == '__main__':
    main()