import algorithms
import utils
import time
from config import *


points_list = utils.load_file_to_list(INPUT_FILE_PATH)
point_index_dict = utils.load_file_to_dict(INPUT_FILE_PATH)
starting_point1 = utils.draw_starting_point(points_list)
starting_point2 = utils.draw_starting_point(points_list)
start_time = time.time()
(res1, tabu_list) = algorithms.nearest_neighbour_alg_for_first_path(starting_point1, points_list, point_index_dict)
res2 = algorithms.nearest_neighbour_alg_for_second_path(starting_point2, points_list, point_index_dict, tabu_list)
points_list_for_permutations_alg = utils.create_points_list_from_indices_list(res1[1], points_list)
(perm_res1, perm_tabu_list, edges_len_list) = algorithms.permutations_fix_for_first_path(starting_point1, points_list_for_permutations_alg, point_index_dict, WINDOW)
points_list_for_permutations_alg_second = utils.create_points_list_from_indices_list(res2[1], points_list)
(perm_res2, edges_len_list_second) = algorithms.permutations_fix_for_second_path(starting_point2, points_list_for_permutations_alg_second, point_index_dict, WINDOW, perm_tabu_list)
end_time = time.time()

utils.save_paths_to_file(perm_res1[1], perm_res2[1], OUTPUT_FILE_PATH_PERMUTATIONS)
utils.save_edges_len_to_file(edges_len_list, edges_len_list_second, EDGES_OUTPUT_FILE_PATH_PERMUTATIONS)
print("Permutations first path length: ", perm_res1[0])
print("Permutations second path length: ", perm_res2[0])
print("Time: ", end_time - start_time)

points_list = utils.load_file_to_list(INPUT_FILE_PATH)
utils.visualize_path(perm_res1[1], points_list)
utils.visualize_path(perm_res2[1], points_list)
