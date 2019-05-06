import algorithms
import utils

INPUT_FILE_PATH = '/home/grzegorznow/Pobrane/santa_cities_test.csv'
OUTPUT_FILE_PATH = '/home/grzegorznow/Pobrane/benchmark_test.csv'
OUTPUT_FILE_PATH_PERMUTATIONS = '/home/grzegorznow/Pobrane/benchmark_test_permutations.csv'

WINDOW = 10

points_list = utils.load_file_to_list(INPUT_FILE_PATH)
point_index_dict = utils.load_file_to_dict(INPUT_FILE_PATH)
starting_point1 = utils.draw_starting_point(points_list)
starting_point2 = utils.draw_starting_point(points_list)
# print(starting_point)

(res1, tabu_list) = algorithms.nearest_neighbour_alg_for_first_path(starting_point1, points_list, point_index_dict)
res2 = algorithms.nearest_neighbour_alg_for_second_path(starting_point2, points_list, point_index_dict, tabu_list)

print(res1)
print(res2)

utils.save_paths_to_file(res1[1], res2[1], OUTPUT_FILE_PATH)

###################################

points_list_for_permutations_alg = utils.create_points_list_from_indices_list(res1[1], points_list)
(perm_res1, perm_tabu_list) = algorithms.permutations_fix_for_first_path(starting_point1, points_list_for_permutations_alg, point_index_dict, WINDOW)
points_list_for_permutations_alg_second = utils.create_points_list_from_indices_list(res2[1], points_list)
perm_res2 = algorithms.permutations_fix_for_second_path(starting_point2, points_list_for_permutations_alg_second, point_index_dict, WINDOW, perm_tabu_list)

utils.save_paths_to_file(perm_res1[1], perm_res2[1], OUTPUT_FILE_PATH_PERMUTATIONS)

print(perm_res1)
print(perm_res2)

print(res1[1] == perm_res1[1])


#  awk 'NR >= 0 && NR <= 1000' /home/grzegorznow/Pobrane/santa_cities.csv > /home/grzegorznow/Pobrane/santa_cities_test.csv