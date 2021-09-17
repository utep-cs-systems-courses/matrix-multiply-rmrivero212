# Ryan Rivero ID:88590478

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

        for i in p.range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
    
    return c


def main():

    a = matrixUtils.genMatrix2(128, 2)
    b = matrixUtils.genMatrix2(128, 2)

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
