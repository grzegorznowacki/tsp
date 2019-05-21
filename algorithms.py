# https://stackoverflow.com/questions/39107896/efficiently-finding-the-closest-coordinate-pair-from-a-set-in-python

# Foreign modules
from scipy import spatial
import itertools
import math
# Our modules
import utils

def find_nearest_neighbour(starting_point, points_list):        # starting point as (x, y)
    tree = spatial.KDTree(points_list)
    result = tree.query([starting_point])
    return (result[0][0], result[1][0])
    # (array([1.41421356]), array([1]))



def nearest_neighbour_alg_for_first_path(starting_point, points_list, point_index_dict):
    path = []
    tabu_list = []

    working_points_list = points_list[:]
    prev_real_index = working_points_list.index(starting_point)
    path.append(working_points_list.index(starting_point))
    working_points_list.remove(starting_point)

    sum_len = 0

    i = 0   # TODO REMOVE

    new_starting_point = starting_point

    while len(working_points_list) > 0:
        found_point_tuple = find_nearest_neighbour(new_starting_point, working_points_list)
        found_point_index = found_point_tuple[1]
        found_point = working_points_list[found_point_index]
        new_starting_point = found_point
        working_points_list.remove(found_point)
        real_index = point_index_dict[found_point]
        path.append(real_index)
        tabu_list.append((prev_real_index, real_index))
        tabu_list.append((real_index, prev_real_index))
        prev_real_index = real_index
        sum_len += found_point_tuple[0]

        i += 1      # TODO REMOVE
        if i % 100 == 0:    # TODO REMOVE
            print(i)    # TODO REMOVE

    return ((sum_len, path), tabu_list)



def nearest_neighbour_alg_for_second_path(starting_point, points_list, point_index_dict, tabu_list):
    path = []

    working_points_list = points_list[:]
    prev_real_index = working_points_list.index(starting_point)
    path.append(working_points_list.index(starting_point))
    working_points_list.remove(starting_point)

    sum_len = 0

    i = 0   # TODO REMOVE

    new_starting_point = starting_point

    while len(working_points_list) > 0:
        working_points_list_inner = working_points_list[:]
        while True:
            found_point_tuple = find_nearest_neighbour(new_starting_point, working_points_list_inner)
            found_point_index = found_point_tuple[1]
            found_point = working_points_list_inner[found_point_index]
            real_index = point_index_dict[found_point]
            if (prev_real_index, real_index) not in tabu_list:
                new_starting_point = found_point
                break
            else:
                working_points_list_inner.remove(found_point)

        working_points_list.remove(found_point)
        path.append(real_index)
        prev_real_index = real_index
        sum_len += found_point_tuple[0]

        i += 1      # TODO REMOVE
        if i % 100 == 0:    # TODO REMOVE
            print(i)    # TODO REMOVE

    return (sum_len, path)




def permutations_fix_for_first_path(starting_point, points_list, point_index_dict, window):
    path = []
    # tabu_list = []

    working_points_list = points_list[:]
    prev_real_index = working_points_list.index(starting_point)
    path.append(working_points_list.index(starting_point))
    # working_points_list.remove(starting_point)

    sum_len = 0

    i = 0   # TODO REMOVE

    new_starting_point = starting_point

    list_of_sublists = [working_points_list[i:i+window] for i in range(0,len(working_points_list),window)]

    new_list = []
    for sublist in list_of_sublists:
        cut_sublist = sublist[1:-1]
        cut_all_permutations = list(itertools.permutations(cut_sublist))
        all_permutations = [[sublist[0]] + list(inner_list) + [sublist[-1]] for inner_list in cut_all_permutations]
        lowest_sum = math.inf
        best_permutation = []
        for permut in all_permutations:
            sum = 0
            for i, j in enumerate(permut[:-1]):
                sum += math.hypot(permut[i + 1][0] - j[0], permut[i+1][1] - j[1])
            if sum <= lowest_sum:
                lowest_sum = sum
                best_permutation = permut[:]
        new_list.extend(best_permutation)


    # while len(working_points_list) > 0:
    #     found_point_tuple = find_nearest_neighbour(new_starting_point, working_points_list)
    #     found_point_index = found_point_tuple[1]
    #     found_point = working_points_list[found_point_index]
    #     new_starting_point = found_point
    #     working_points_list.remove(found_point)
    #     real_index = point_index_dict[found_point]
    #     path.append(real_index)
    #     tabu_list.append((prev_real_index, real_index))
    #     tabu_list.append((real_index, prev_real_index))
    #     prev_real_index = real_index
    #     sum_len += found_point_tuple[0]
    #
    #     i += 1      # TODO REMOVE
    #     if i % 100 == 0:    # TODO REMOVE
    #         print(i)    # TODO

    total_length = 0
    for i, j in enumerate(new_list[:-1]):
        total_length += math.hypot(new_list[i + 1][0] - j[0], new_list[i + 1][1] - j[1])

    new_list_indices = [point_index_dict[point] for point in new_list]

    tabu_list = []
    for i, j in enumerate(new_list_indices[:-1]):
        tabu_list.append((j, new_list_indices[i + 1]))
        tabu_list.append((new_list_indices[i+1], j))

    return ((total_length, new_list_indices), tabu_list)




def permutations_fix_for_second_path(starting_point, points_list, point_index_dict, window, tabu_list):
    path = []
    # tabu_list = []

    working_points_list = points_list[:]
    prev_real_index = working_points_list.index(starting_point)
    path.append(working_points_list.index(starting_point))
    # working_points_list.remove(starting_point)

    sum_len = 0

    i = 0   # TODO REMOVE

    new_starting_point = starting_point

    list_of_sublists = [working_points_list[i:i+window] for i in range(0,len(working_points_list),window)]

    new_list = []
    for sublist in list_of_sublists:
        cut_sublist = sublist[1:-1]
        cut_all_permutations = list(itertools.permutations(cut_sublist))
        all_permutations = [[sublist[0]] + list(inner_list) + [sublist[-1]] for inner_list in cut_all_permutations]
        lowest_sum = math.inf
        best_permutation = []
        for permut in all_permutations:
            sum = 0
            for i, j in enumerate(permut[:-1]):
                sum += math.hypot(permut[i + 1][0] - j[0], permut[i+1][1] - j[1])
            if sum <= lowest_sum and (permut[i+1], j) not in tabu_list:
                lowest_sum = sum
                best_permutation = permut[:]
        if not best_permutation:
            print("ERROR - empty")
        new_list.extend(best_permutation)


    # while len(working_points_list) > 0:
    #     found_point_tuple = find_nearest_neighbour(new_starting_point, working_points_list)
    #     found_point_index = found_point_tuple[1]
    #     found_point = working_points_list[found_point_index]
    #     new_starting_point = found_point
    #     working_points_list.remove(found_point)
    #     real_index = point_index_dict[found_point]
    #     path.append(real_index)
    #     tabu_list.append((prev_real_index, real_index))
    #     tabu_list.append((real_index, prev_real_index))
    #     prev_real_index = real_index
    #     sum_len += found_point_tuple[0]
    #
    #     i += 1      # TODO REMOVE
    #     if i % 100 == 0:    # TODO REMOVE
    #         print(i)    # TODO

    total_length = 0
    for i, j in enumerate(new_list[:-1]):
        total_length += math.hypot(new_list[i + 1][0] - j[0], new_list[i + 1][1] - j[1])

    new_list_indices = [point_index_dict[point] for point in new_list]

    return (total_length, new_list_indices)





# l = [(1,2), (3,4), (5,6)]
# print(find_nearest_neighbour((10,10), l))


#
# def nearest_neighbour_alg(starting_point_index, points_dict):
#     del points_dict[starting_point_index]
#     # find_nearest_neighbour(starting_point, working_points_list)



# TODO wykorzystac normalna lsite tuplei i odwrocony slownik tupla -> index


# def square_fix_for_first_path(starting_points, bucket_points_list):
#     points_lists = []
#     for elem in bucket_points_list:
#         points_lists.append(elem[1])
#     points_path_list = []
#     for starting_point, points_list in zip(starting_points, points_lists):
#         path = []
#         tabu_list = []
#
#         working_points_list = points_list[:]
#         prev_found_point = starting_point
#         path.append(starting_point)
#         working_points_list.remove(starting_point)
#
#         sum_len = 0
#
#         i = 0   # TODO REMOVE
#
#         new_starting_point = starting_point
#
#         while len(working_points_list) > 0:
#             found_point_tuple = find_nearest_neighbour(new_starting_point, working_points_list)
#             found_point_index = found_point_tuple[1]
#             found_point = working_points_list[found_point_index]
#             new_starting_point = found_point
#             working_points_list.remove(found_point)
#             path.append(found_point)
#             tabu_list.append((prev_found_point, found_point))
#             tabu_list.append((found_point, prev_found_point))
#             prev_found_point = found_point
#             sum_len += found_point_tuple[0]
#
#             i += 1      # TODO REMOVE
#             if i % 100 == 0:    # TODO REMOVE
#                 print(i)    # TODO REMOVE
#
#         points_path_list.append(((sum_len, path), tabu_list))
#
#     return points_path_list


def square_fix_for_first_path(starting_points, bucket_points_list):
    points_lists = []
    for elem in bucket_points_list:
        points_lists.append(elem[1])

    point_index_dicts = []
    for inner_list in points_lists:
        point_index_dict = {}
        for elem in inner_list:
            point_index_dict[elem] = inner_list.index(elem)
        point_index_dicts.append(point_index_dict)

    ### starting_points, points_lists, point_index_dicts

    results_list = []
    for starting_point, points_list, point_index_dict in zip(starting_points, points_lists, point_index_dicts):
        result = nearest_neighbour_alg_for_first_path(starting_point, points_list, point_index_dict)
        results_list.append(result)

    return results_list

def square_fix_for_second_path(starting_points, bucket_points_list, tabu_list_all):
    points_lists = []
    for elem in bucket_points_list:
        points_lists.append(elem[1])

    point_index_dicts = []
    for inner_list in points_lists:
        point_index_dict = {}
        for elem in inner_list:
            point_index_dict[elem] = inner_list.index(elem)
        point_index_dicts.append(point_index_dict)

    ### starting_points, points_lists, point_index_dicts

    results_list = []
    for starting_point, points_list, point_index_dict in zip(starting_points, points_lists, point_index_dicts):
        result = nearest_neighbour_alg_for_second_path(starting_point, points_list, point_index_dict, tabu_list_all)
        results_list.append(result)

    return results_list

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

        for tabu_elem in tabu_inner_list:
            tabu_point_tuple = (points_list[tabu_elem[0]], points_list[tabu_elem[1]])
            global_tabu_index_tuple = (point_index_dict_all[tabu_point_tuple[0]], point_index_dict_all[tabu_point_tuple[1]])
            tabu_list_all.append(global_tabu_index_tuple)

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
    prev_point = points_list_all[indices_list_all[0]]
    for index in indices_list_all[1:]:
        path_len += math.hypot(points_list_all[index][0] - prev_point[0], points_list_all[index][1] - prev_point[1])
        prev_point = points_list_all[index]
    return path_len