import algorithms
import utils

INPUT_FILE_PATH = '/home/grzegorznow/Pobrane/santa_cities_test.csv'

points_list = utils.load_file_to_list(INPUT_FILE_PATH)
point_index_dict = utils.load_file_to_dict(INPUT_FILE_PATH)
starting_point = utils.draw_starting_point(points_list)
print(starting_point)

res = algorithms.nearest_neighbour_alg((15930, 5604), points_list, point_index_dict)

print(res)



#  awk 'NR >= 0 && NR <= 1000' /home/grzegorznow/Pobrane/santa_cities.csv > /home/grzegorznow/Pobrane/santa_cities_test.csv