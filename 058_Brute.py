#Brute Force Method
from __future__ import division

import time 
import math
import numpy as np

start = time.time()

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {N: E, E: S, S: W, W: N} # old -> new direction

def spiral(width,height):
    if width<1 or height<1:
        raise ValueError
    x, y = width//2 , height//2
    dx, dy = N #initial direction
    matrix = [[None] *width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count #visit
        #try to turn right 
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x+new_dx, y+new_dy
        if (0<=new_x<width and 0<=new_y<height and matrix[new_y][new_x] is None):
            x,y = new_x,new_y
            dx,dy = new_dx,new_dy
        else:
            x,y = x+dx,y+dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # end of matrix, reached last element


def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))

def is_prime(n):
    # n = abs(n)
    if n<=1: 
        return False
    for i in range(2,(int(math.sqrt(n))+1)):
        if n%i == 0:
            return False
            break
    return True

def main():
    n = 3
    ratio = 100.00
    while(ratio >= 0.1):

        spiral_matrix = spiral(n,n)
        diagonal = np.diagonal(spiral_matrix) 
        reverse_diagonal = np.diag(np.fliplr(spiral_matrix))
        
        count_primes = 0
        for element in diagonal:
            if is_prime(element):
                count_primes += 1
        for reverse_element in reverse_diagonal[-len(reverse_diagonal)//2:]:
            if is_prime(reverse_element):
                count_primes += 1
  
        ratio  = count_primes/((2*n) - 1) 
        print(n,ratio,count_primes)
        n += 2

    return n
 
elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed)) 


