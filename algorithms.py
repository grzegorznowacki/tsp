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



def nearest_neighbour_alg(starting_point, points_list, point_index_dict):
    path = []

    working_points_list = points_list[:]
    path.append(working_points_list.index(starting_point))
    working_points_list.remove(starting_point)

    sum_len = 0

    while len(working_points_list) > 0:
        found_point_tuple = find_nearest_neighbour(starting_point, working_points_list)
        found_point_index = found_point_tuple[1]
        found_point = working_points_list[found_point_index]
        working_points_list.remove(found_point)
        real_index = point_index_dict[found_point]
        path.append(real_index)
        sum_len += found_point_tuple[0]

    return (sum_len, path)

# l = [(1,2), (3,4), (5,6)]
# print(find_nearest_neighbour((10,10), l))


#
# def nearest_neighbour_alg(starting_point_index, points_dict):
#     del points_dict[starting_point_index]
#     # find_nearest_neighbour(starting_point, working_points_list)



# TODO wykorzystac normalna lsite tuplei i odwrocony slownik tupla -> index