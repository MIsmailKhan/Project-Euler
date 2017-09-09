import math
import time 
start = time.time()

def read_data(path):

    file = open(path,mode='r').read() #read converts the read object into a string
    # print(str(file))
    data = filter(None,list(file.split('\n')))
    matrix = [[]]
    for index,entry in enumerate(data):
        entry.replace(" ","")
        matrix.append(map(int,list(entry.split(','))))
    return filter(None,matrix)


def euler82(matrix):
    nrows, ncols = len(matrix), len(matrix[0])
    best = [matrix[row][0] for row in range(nrows)]

    for col in range(1, ncols):
        column = [matrix[row][col] for row in range(nrows)]

        best = [
            # The cost of each cell, plus...
            column[row] +

            # the cost of the cheapest approach to it
            min([
                best[prev_row] + sum(column[prev_row:row:(1 if prev_row <= row else -1)])
                for prev_row in range(nrows)
            ])
            for row in range(nrows)
        ]

        #print(best)

    return min(best)


def main():
    data_matrix = read_data('p082_matrix.txt')
    return euler82(data_matrix)

elapsed = time.time() - start
print ("%s found in %s seconds" % (main(),elapsed))