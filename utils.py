import csv
import random
from random import randint

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