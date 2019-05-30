import algorithms
import utils
import algorithms_utils
import time
from config import *


points_list = utils.load_file_to_list(INPUT_FILE_PATH)
start_time = time.time()
outer_square_size = utils.find_outer_square_size(points_list)
divided_range_list = utils.divide_range(SQUARE_DIVIDOR, start=0, end=outer_square_size)
buckets_list = utils.create_buckets(divided_range_list)
bucket_points_list = utils.list_bucketing(points_list, buckets_list)
starting_points_in_squares_list = utils.find_starting_point_for_square(bucket_points_list)
square_results_list = algorithms.square_fix_for_first_path(starting_points_in_squares_list, bucket_points_list)
point_index_dict_all = utils.load_file_to_dict(INPUT_FILE_PATH)
indices_list_all, tabu_list_all = algorithms_utils.calculate_square_fix_result_first(bucket_points_list, square_results_list, point_index_dict_all)
points_list_all = utils.load_file_to_list(INPUT_FILE_PATH)
path_len = algorithms_utils.calculate_path_length_based_on_indices_path_list(indices_list_all, points_list_all)
### second path ###
square_results_list_second = algorithms.square_fix_for_second_path(starting_points_in_squares_list, bucket_points_list, tabu_list_all)
indices_list_all_second = algorithms_utils.calculate_square_fix_result_second(bucket_points_list, square_results_list_second, point_index_dict_all)
path_len_second = algorithms_utils.calculate_path_length_based_on_indices_path_list(indices_list_all_second, points_list_all)
end_time = time.time()

utils.save_paths_to_file(indices_list_all, indices_list_all_second, OUTPUT_FILE_PATH_SQUARES)
print("Squares first path length: ", path_len)
print("Squares second path length: ", path_len_second)
print("Time: ", end_time - start_time)




