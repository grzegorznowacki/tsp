import algorithms
import utils
import time
from config import *


points_list = utils.load_file_to_list(INPUT_FILE_PATH)
point_index_dict = utils.load_file_to_dict(INPUT_FILE_PATH)
starting_point1 = utils.draw_starting_point(points_list)
starting_point2 = utils.draw_starting_point(points_list)
start_time = time.time()
(res1, tabu_list, edges_len_list) = algorithms.nearest_neighbour_alg_for_first_path(starting_point1, points_list, point_index_dict)
(res2, edges_len_list_second) = algorithms.nearest_neighbour_alg_for_second_path(starting_point2, points_list, point_index_dict, tabu_list)
end_time = time.time()

utils.save_paths_to_file(res1[1], res2[1], OUTPUT_FILE_PATH)
utils.save_edges_len_to_file(edges_len_list, edges_len_list_second, EDGES_OUTPUT_FILE_PATH)
print("Nearest neighbour first path length: ", res1[0])
print("Nearest neighbour second path length: ", res2[0])
print("Time: ", end_time - start_time)

points_list = utils.load_file_to_list(INPUT_FILE_PATH)
utils.visualize_path(res1[1], points_list)
utils.visualize_path(res2[1], points_list)



