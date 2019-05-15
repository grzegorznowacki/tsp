import algorithms
import utils

INPUT_FILE_PATH = '/home/grzegorznow/Pobrane/santa_cities_test.csv'
OUTPUT_FILE_PATH = '/home/grzegorznow/Pobrane/benchmark_test.csv'
OUTPUT_FILE_PATH_PERMUTATIONS = '/home/grzegorznow/Pobrane/benchmark_test_permutations.csv'

WINDOW = 10

SQUARE_DIVIDOR = 5000

points_list = utils.load_file_to_list(INPUT_FILE_PATH)

outer_square_size = utils.find_outer_square_size(points_list)
print(outer_square_size)
print(outer_square_size)

divided_range_list = utils.divide_range(SQUARE_DIVIDOR, start=0, end=outer_square_size)
print(divided_range_list)
buckets_list = utils.create_buckets(divided_range_list)
print(buckets_list)

bucket_points_list = utils.list_bucketing(points_list, buckets_list)
print(bucket_points_list)

