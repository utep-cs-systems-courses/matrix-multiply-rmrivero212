import matrixUtils
import numpy as np
import time
import pymp

def matrixMultiply(a, b):
    
    c = np.zeros((a.shape[0], b.shape[1]), dtype = np.int16)

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def matrixMultiplyPar(a, b):

    c = np.zeros((a.shape[0], b.shape[1]), dtype = np.int16)
    
    with pymp.Parallel() as p:

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in p.range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
        
    return c
"""
def blocked(a, b):
    tile_size = 16

    for kk in len(a) step tile_size:
        for jj in len(b[0]) step tile_size:
            for i in len(b):
                j_end_val = jj + tile_size
                for j in range(jj, j_end_val):
                    k_end_val = kk + tile_size:
                    sum = output[i][j]
                    for k in range(kk, k_end_val):
                        sum = sum + in_a[i][k] * in_b[k][j]
                    output[i][j] =  sum
    return output
"""
def main():

    a = matrixUtils.genMatrix2(32, 2);
    b = matrixUtils.genMatrix2(32, 2)

    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    MMP = matrixMultiply(a, b)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    
    startPar = time.clock_gettime(time.CLOCK_MONOTONIC)
    MM = matrixMultiplyPar(a, b)
    endPar = time.clock_gettime(time.CLOCK_MONOTONIC)
    
    print('New Matrix:')
    print(MM)
    print("Time to process using regular Matrix Multiply: ", str(end - start))
    print("Time to process using Parallized Matrix Multiply: ", str(endPar - startPar))

if __name__ =='__main__':
    main()
