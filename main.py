import algorithms
import utils

INPUT_FILE_PATH = '/home/grzegorznow/Pobrane/santa_cities_test.csv'
OUTPUT_FILE_PATH = '/home/grzegorznow/Pobrane/benchmark_test.csv'

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



#  awk 'NR >= 0 && NR <= 1000' /home/grzegorznow/Pobrane/santa_cities.csv > /home/grzegorznow/Pobrane/santa_cities_test.csv