import matrixUtils
import numpy as np
import time

def matrixMultiply(a, b):

    tp = np.zeros((a.shape[0], b.shape[1]), dtype = np.int16)
    c = tp.reshape(a.shape[0], b.shape[1])

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):r
                c[i][j] += a[i][k] * b[k][j]
    return c

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
