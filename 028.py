import time 
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

spiral_matrix = spiral(1001,1001)
diagonal = np.diagonal(spiral_matrix)
reverse_diagonal = np.diag(np.fliplr(spiral_matrix))
solution = sum(diagonal) + sum(reverse_diagonal) -1  #1 is repeated twice 
 
elapsed = time.time() - start
print ("%s found in %s seconds" % (solution,elapsed)) 


