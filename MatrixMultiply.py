import matrixUtils
import numpy as np
import time

def matrixMultiply(a, b):

    tp = np.zeros((a.shape[0], b.shape[1]), dtype = np.int16)
    c = tp.reshape(a.shape[0], b.shape[1])

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def main():


    tmp1 = np.arange(1, 17)
    tmp2 = np.arange(16, 32)
    a = tmp1.reshape(4, 4)
    b = tmp2.reshape(4, 4)

    print(a)
    print(b)

    start = time.clock_gettime(time.CLOCK_MONOTONIC)
    c = matrixMultiply(a, b)
    end = time.clock_gettime(time.CLOCK_MONOTONIC)
    print('New Matrix:')
    print(c)
    print("Time to process: ", str(end - start))


if __name__ =='__main__':
    main()
