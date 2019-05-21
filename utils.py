import csv
import random
from random import randint
from itertools import groupby
import algorithms

def load_file_to_list(input_file_path):
    points_list = []
    with open(input_file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            points_list.append((int(row[1]), int(row[2])))
    return points_list

def load_file_to_dict(input_file_path):
    point_index_dict = {}
    with open(input_file_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            point_index_dict[(int(row[1]), int(row[2]))] = int(row[0])
    return point_index_dict

def draw_starting_point(points_list):
    return random.choice(points_list)



def draw_starting_point_index(points_list):
    return randint(0, len(points_list) - 1)


def save_paths_to_file(found_path1, found_path2, output_file_path):
    with open(output_file_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['path1', 'path2'])
        for index1, index2 in zip(found_path1, found_path2):
            writer.writerow([index1, index2])


def create_points_list_from_indices_list(indices_list, points_list_from_file):
    result_points_list = []
    for index in indices_list:
        result_points_list.append(points_list_from_file[index])
    return result_points_list

##############################################################################

def find_outer_square_size(points_list):
    max_x = 0
    max_y = 0
    for point in points_list:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
    if max_x >= max_y:
        return max_x
    else:
        return max_y

def divide_range(portion, start=0, end=2**32):
    threshold_list_start = []
    threshold_list_end = []
    for i in range(start, end, portion):
        threshold_list_start.append(i+1)
        threshold_list_end.append(i)
    threshold_list_start[0] = start
    threshold_list_end = threshold_list_end[1:]
    threshold_list_end.append(end)
    ip_range_list = list(zip(threshold_list_start, threshold_list_end))
    return ip_range_list

def create_buckets(divided_range_list):
    buckets_list = []
    for range_x in divided_range_list:
        for range_y in divided_range_list:
            buckets_list.append((range_x, range_y))
    return buckets_list

def list_bucketing(points_list, buckets_list):
    bucket_points_dict = dict()
    bucket_points_list = []
    for point in points_list:
        for bucket in buckets_list:
            if bucket[0][0] <= point[0] <= bucket[0][1] and bucket[1][0] <= point[1] <= bucket[1][1]:
                if bucket not in bucket_points_dict:
                    bucket_points_dict[bucket] = [point]
                else:
                    bucket_points_dict[bucket].append(point)
    for key in sorted(bucket_points_dict.keys()):
        bucket_points_list.append((key, bucket_points_dict[key]))
        print(key)
    bucket_points_list = [list(grp) for k, grp in groupby(bucket_points_list)]
    bucket_points_list_final = []
    for elem in bucket_points_list:
        [unpacked_elem] = elem
        bucket_points_list_final.append(unpacked_elem)

    return bucket_points_list_final

def find_starting_point_for_square(bucket_points_list):
    starting_points_in_squares_list = []
    for bucket_pointslist_tuple in bucket_points_list:
        edge_coords = (bucket_pointslist_tuple[0][0][0], bucket_pointslist_tuple[0][1][0])
        starting_point_index = algorithms.find_nearest_neighbour(edge_coords, bucket_pointslist_tuple[1])[1]
        starting_point = bucket_pointslist_tuple[1][starting_point_index]
        starting_points_in_squares_list.append(starting_point)
    return starting_points_in_squares_list