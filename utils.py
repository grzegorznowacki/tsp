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

