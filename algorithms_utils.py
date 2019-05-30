from scipy import spatial
import math


def find_nearest_neighbour(starting_point, points_list):        # starting point as (x, y)
    tree = spatial.KDTree(points_list)
    result = tree.query([starting_point])
    return (result[0][0], result[1][0])
    # (array([1.41421356]), array([1]))


def calculate_square_fix_result_first(bucket_points_list, square_results_list, point_index_dict_all):
    points_lists = []
    for elem in bucket_points_list:
        points_lists.append(elem[1])

    indices_list_all = []
    tabu_list_all = []
    for points_list, elem in zip(points_lists, square_results_list):
        inner_list = elem[0][1]
        tabu_inner_list = elem[1]
        for index in inner_list:
            point = points_list[index]
            global_index = point_index_dict_all[point]
            indices_list_all.append(global_index)
        tabu_list_all.append(tabu_inner_list)

    return (indices_list_all, tabu_list_all)


def calculate_square_fix_result_second(bucket_points_list, square_results_list, point_index_dict_all):
    points_lists = []
    for elem in bucket_points_list:
        points_lists.append(elem[1])

    indices_list_all = []
    for points_list, elem in zip(points_lists, square_results_list):
        inner_list = elem[1]
        for index in inner_list:
            point = points_list[index]
            global_index = point_index_dict_all[point]
            indices_list_all.append(global_index)

    return indices_list_all


def calculate_path_length_based_on_indices_path_list(indices_list_all, points_list_all):
    path_len = 0
    edges_len_list = []
    prev_point = points_list_all[indices_list_all[0]]
    for index in indices_list_all[1:]:
        edge_len = math.hypot(points_list_all[index][0] - prev_point[0], points_list_all[index][1] - prev_point[1])
        path_len += edge_len
        edges_len_list.append(edge_len)
        prev_point = points_list_all[index]
    return (path_len, edges_len_list)

