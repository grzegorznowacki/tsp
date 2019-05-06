# https://stackoverflow.com/questions/39107896/efficiently-finding-the-closest-coordinate-pair-from-a-set-in-python

# Foreign modules
from scipy import spatial
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




# l = [(1,2), (3,4), (5,6)]
# print(find_nearest_neighbour((10,10), l))


#
# def nearest_neighbour_alg(starting_point_index, points_dict):
#     del points_dict[starting_point_index]
#     # find_nearest_neighbour(starting_point, working_points_list)



# TODO wykorzystac normalna lsite tuplei i odwrocony slownik tupla -> index