# tsp
## Travelling  Santa Problem Solvers
### Input
CSV file containing points coordinates:
```csv
id,x,y
0,4360,6178
1,10906,14956
2,5071,8963
3,13853,4105
4,18885,3168
5,7439,14160
```
### Output
CSV file containing paths consisting of points indices:
```csv
path1,path2
570,185
415,7
608,891
464,484
700,777
993,515
99,80
217,571
725,40
105,353
```
### How to trim sample benchmark file:
```bash
awk 'NR >= 0 && NR <= 1000' input/santa_cities.csv > input/santa_cities_trimmed.csv
```
### How to configurate app:
#### See config.py
- Common
    - INPUT_FILE_PATH
- Nearest neighbour 
    - OUTPUT_FILE_PATH
- Permutations
    - OUTPUT_FILE_PATH_PERMUTATIONS
    - WINDOW
- Squares
    - OUTPUT_FILE_PATH_SQUARES
    - SQUARE_DIVIDOR
### How to launch app:
```bash
python3 main_nearest_neighbour.py
python3 main_permutations.py
python3 main_squares.py
```
### Documentation
See **docs** directory.
