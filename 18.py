#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import os
'''
I am not proud of this or how long it took to write
'''

#returns string of binary integer from decimal integer
def to_bin(number):
    bin_str = str(bin(number))[2:]
    return bin_str

#used to generate maps
def nth_tri_num(n):
    num = 1/2 * n * (n + 1)
    return int(num)

#used also to generate maps
def tri_num_to_n(num):
    n = (2 * num + 1/4) ** (1/2) - 1/2
    return int(n)

#move down and left or down and right
def move_l(current_coord):
    next_coord = [current_coord[0],current_coord[1] + 1]
    return next_coord

def move_r(current_coord):
    next_coord = [current_coord[0] + 1,current_coord[1] + 1]
    return next_coord

#brute checks all possible paths within a triangle and picks the one with the highest value
def brute(map):
    possible_paths = {}
    
    move_queue = 2**(len(map) - 1) - 1
    
    while True:
        current_path = [[0,0]]
        Sum = map[0][0]
        
        #iterable is move_queue but with zeroes in the front. if o_m_q was 111 and move_queue is 10, iterable'll be 010
        move_cue = [int(digit)
                    for digit in to_bin(move_queue)]
        #fuck reading numbers from left to right. easier right to left for programming
        iterable = [0
                    if i - ((len(map) - 1) - len(move_cue)) < 0
                    else move_cue[i - ((len(map) - 1) - len(move_cue))]
                    for i in range(len(map) - 1)]
        
        #for every digit in move_queue, move left if the digit is zero, right if 1
        for digit in iterable:
            if digit == 0:
                current_path.append(move_l([current_path[-1][0],current_path[-1][1]]))
            if digit == 1:
                current_path.append(move_r([current_path[-1][0],current_path[-1][1]]))
            Sum += map[current_path[-1][1]][current_path[-1][0]]
        
        possible_paths[move_queue] = Sum
        
        if move_queue == 0:
            break
        
        move_queue -= 1
    
    final_route = max(possible_paths,key = possible_paths.get)
    
    return [final_route,possible_paths[final_route]]

'''
source = "75 95 64 17 47 82 18 35 87 10 20 04 82 47 65 19 01 23 75 03 34 88 02 77 73 07 63 67 99 65 04 28 06 16 70 92 41 41 26 56 83 40 80 70 33 41 48 72 33 47 32 37 16 94 29 53 71 44 65 25 43 91 52 97 51 14 70 11 33 28 77 73 17 78 39 68 17 57 91 71 52 38 17 14 91 43 58 50 27 29 48 63 66 04 68 89 53 67 30 73 16 69 87 40 31 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
'''

os.chdir("/storage/emulated/0/qpython/scripts3/Project_Euler")
f = open('triangle.txt', 'r')
lines = f.readlines()

source = " ".join([line.strip() for line in lines])

source = source.split()
source = [int(number)
          for number in source]
tri_map = [source[nth_tri_num(i) - i:nth_tri_num(i)]
           for i in range(1,tri_num_to_n(len(source)) + 1)]

look_ahead = 14#int(len(tri_map) // len(tri_map) ** 1/2)

#using look ahead and brute force
route = [[0,0]]
while route[-1][1] != (len(tri_map) - 1):
    #progress report!!!
    #print("At: ({}, {})".format(route[-1][0],route[-1][1]))
    
    if route[-1][1] + look_ahead < len(tri_map) - 1:
        map_ahead = [tri_map[route[-1][1] + i][route[-1][0]:route[-1][0] + (i + 1)]
                     for i in range(look_ahead)]
    else:
        map_ahead = [tri_map[route[-1][1] + i][route[-1][0]:route[-1][0] + (i + 1)]
                     for i in range(len(tri_map) - route[-1][1])]
    
    look_path = [int(digit)
                 for digit in to_bin(brute(map_ahead)[0])]
    iterable = [0
                if i - ((len(map_ahead) - 1) - len(look_path)) < 0
                else look_path[i - ((len(map_ahead) - 1) - len(look_path))]
                for i in range(len(map_ahead) - 1)]
    
    look_path = [[route[-1][0],route[-1][1]]]
    
    for digit in iterable:
        if digit == 0:
            look_path.append(move_l([look_path[-1][0],look_path[-1][1]]))
        if digit == 1:
            look_path.append(move_r([look_path[-1][0],look_path[-1][1]]))
    
    for coord in look_path[1:]:
        route.append(coord)


parts = [tri_map[coord[1]][coord[0]]
         for coord in route]
print(sum(parts))