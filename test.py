import algorithms
import utils

INPUT_FILE_PATH = '/home/gnowacki/Pobrane/santa_cities_test.csv'
OUTPUT_FILE_PATH = '/home/gnowacki/Pobrane/benchmark_test.csv'
OUTPUT_FILE_PATH_PERMUTATIONS = '/home/gnowacki/Pobrane/benchmark_test_permutations.csv'

SQUARE_DIVIDOR = 4

points_list = utils.load_file_to_list(INPUT_FILE_PATH)

outer_square_size = utils.find_outer_square_size(points_list)
print(outer_square_size)
print(outer_square_size)

square_dividor = outer_square_size / SQUARE_DIVIDOR

divided_range_list = utils.divide_range(SQUARE_DIVIDOR, start=0, end=outer_square_size)
print(divided_range_list)
buckets_list = utils.create_buckets(divided_range_list)
print(buckets_list)

bucket_points_list = utils.list_bucketing(points_list, buckets_list)
print("bucket_points_list")
print(bucket_points_list)
print(bucket_points_list[0])
print(bucket_points_list[0][0])
print(bucket_points_list[0][1])
print("#####################")

# for i in bucket_points_list:
#     print(len(i[1]))

starting_points_in_squares_list = utils.find_starting_point_for_square(bucket_points_list)
print(starting_points_in_squares_list)

square_results_list = algorithms.square_fix_for_first_path(starting_points_in_squares_list, bucket_points_list)

# for i in square_results_list:
#     print(i)

point_index_dict_all = utils.load_file_to_dict(INPUT_FILE_PATH)

indices_list_all, tabu_list_all = algorithms.calculate_square_fix_result_first(bucket_points_list, square_results_list, point_index_dict_all)

print(indices_list_all)
print(tabu_list_all)
print(len(indices_list_all))

points_list_all = utils.load_file_to_list(INPUT_FILE_PATH)
path_len = algorithms.calculate_path_length_based_on_indices_path_list(indices_list_all, points_list_all)
print(path_len)

### second path
square_results_list_second = algorithms.square_fix_for_second_path(starting_points_in_squares_list, bucket_points_list, tabu_list_all)
print(square_results_list)
print(square_results_list_second)
indices_list_all_second = algorithms.calculate_square_fix_result_second(bucket_points_list, square_results_list_second, point_index_dict_all)
path_len_second = algorithms.calculate_path_length_based_on_indices_path_list(indices_list_all_second, points_list_all)

print(indices_list_all)
print(indices_list_all_second)
print(path_len)
print(path_len_second)

print(indices_list_all)


