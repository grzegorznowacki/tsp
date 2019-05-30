import itertools
import math
import algorithms_utils


def nearest_neighbour_alg_for_first_path(starting_point, points_list, point_index_dict):
    path = []
    tabu_list = []
    edges_len_list = []

    working_points_list = points_list[:]
    prev_real_index = working_points_list.index(starting_point)
    path.append(working_points_list.index(starting_point))
    working_points_list.remove(starting_point)

    sum_len = 0

    new_starting_point = starting_point

    while len(working_points_list) > 0:
        found_point_tuple = algorithms_utils.find_nearest_neighbour(new_starting_point, working_points_list)
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
        edges_len_list.append(found_point_tuple[0])

    return ((sum_len, path), tabu_list, edges_len_list)


def nearest_neighbour_alg_for_second_path(starting_point, points_list, point_index_dict, tabu_list):
    path = []
    edges_len_list = []

    working_points_list = points_list[:]
    prev_real_index = working_points_list.index(starting_point)
    path.append(working_points_list.index(starting_point))
    working_points_list.remove(starting_point)

    sum_len = 0

    new_starting_point = starting_point

    while len(working_points_list) > 0:
        working_points_list_inner = working_points_list[:]
        while True:
            if not working_points_list_inner:
                break
            found_point_tuple = algorithms_utils.find_nearest_neighbour(new_starting_point, working_points_list_inner)
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
        edges_len_list.append(found_point_tuple[0])

    return ((sum_len, path), edges_len_list)


def permutations_fix_for_first_path(starting_point, points_list, point_index_dict, window):
    path = []
    edges_len_list = []

    working_points_list = points_list[:]
    path.append(working_points_list.index(starting_point))

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

    total_length = 0
    for i, j in enumerate(new_list[:-1]):
        edge_len = math.hypot(new_list[i + 1][0] - j[0], new_list[i + 1][1] - j[1])
        total_length += edge_len
        edges_len_list.append(edge_len)

    new_list_indices = [point_index_dict[point] for point in new_list]

    tabu_list = []
    for i, j in enumerate(new_list_indices[:-1]):
        tabu_list.append((j, new_list_indices[i + 1]))
        tabu_list.append((new_list_indices[i+1], j))

    return ((total_length, new_list_indices), tabu_list, edges_len_list)


def permutations_fix_for_second_path(starting_point, points_list, point_index_dict, window, tabu_list):
    path = []
    edges_len_list = []

    working_points_list = points_list[:]
    path.append(working_points_list.index(starting_point))

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

    total_length = 0
    for i, j in enumerate(new_list[:-1]):
        edge_len = math.hypot(new_list[i + 1][0] - j[0], new_list[i + 1][1] - j[1])
        total_length += edge_len
        edges_len_list.append(edge_len)

    new_list_indices = [point_index_dict[point] for point in new_list]

    return ((total_length, new_list_indices), edges_len_list)


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


def square_fix_for_second_path(starting_points, bucket_points_list, tabu_lists):
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
    for starting_point, points_list, point_index_dict, tabu_list in zip(starting_points, points_lists, point_index_dicts, tabu_lists):
        result = nearest_neighbour_alg_for_second_path(starting_point, points_list, point_index_dict, tabu_list)
        results_list.append(result)

    return results_list


