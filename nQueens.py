# coding=utf-8

import pycosat

def get_nQueen_CNFs(n):
    # cell = 0 = no Queen = idx
    #  1  2  3  4
    #  5  6  7  8
    #  9 10 11 12
    # 13 14 15 16

    # cell = 1 = Queen = idx + n*n*1
    # 17 18 19 20
    # 21 22 23 24
    # 25 26 27 28
    # 29 30 31 32 

    CNFs = []
    m = n*n

    # at least one "True" per cell
    # [[1, 17], [2, 18], [3, 19], [4, 20], [5, 21], [6, 22], [7, 23], [8, 24], [9, 25], [10, 26], [11, 27], [12, 28], [13, 29], [14, 30], [15, 31], [16, 32]]
    for i in range(1, m+1):
        CNFs += [[i, i+m]]

    # no more than one "True" per cell
    # [[-1, -17], [-2, -18], [-3, -19], [-4, -20], [-5, -21], [-6, -22], [-7, -23], [-8, -24], [-9, -25], [-10, -26], [-11, -27], [-12, -28], [-13, -29], [-14, -30], [-15, -31], [-16, -32]]
    for i in range(1, m+1):
        CNFs += [[-i, -(i+m)]]

    # at least one "True" per row
    # [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]
    for i in range(m+1, 2*m+1, n):
        CNF = []
        for j in range(0, n):
            CNF += [i+j]
        CNFs += [CNF]

    # no more than one "True" per row
    # [-17, -18], [-17, -19], [-17, -20],  [-18, -19], [-18, -20],  [-19, -20], 
    # [-21, -22], [-21, -23], [-21, -24],  [-22, -23], [-22, -24],  [-23, -24], 
    # [-25, -26], [-25, -27], [-25, -28],  [-26, -27], [-26, -28],  [-27, -28], 
    # [-29, -30], [-29, -31], [-29, -32],  [-30, -31], [-30, -32],  [-31, -32]
    for i in range(m+1, 2*m+1, n):     # i = 17, 21, 25, 29
        for j in range(1, n):        # j = 1, 2, 3
            for k in range(j, n):    # k = 1, 2, 3, 2, 3, 3
              CNFs += [[-(i+j-1), -(i+k)]]

    # at least one "True" per column
    # [[17, 21, 25, 29], [18, 22, 26, 30], [19, 23, 27, 31], [20, 24, 28, 32]]
    for i in range(m+1, m+n+1):
        CNF = []
        for j in range(0, m, n):
            CNF += [i+j]
        CNFs += [CNF]

    # no more than one "True" per column
    # [-17, -21], [-17, -25], [-17, -29],  [-21, -25], [-21, -29],  [-25, -29], 
    # [-18, -22], [-18, -26], [-18, -30],  [-22, -26], [-22, -30],  [-26, -30], 
    # [-19, -23], [-19, -27], [-19, -31],  [-23, -27], [-23, -31],  [-27, -31], 
    # [-20, -24], [-20, -28], [-20, -32],  [-24, -28], [-24, -32],  [-28, -32]
    for i in range(m+1, m+n+1):     # i = 17, 18, 19, 20
        for j in range(1, n):        # j = 1, 2, 3
            for k in range(j, n):    # k = 1, 2, 3, 2, 3, 3
              CNFs += [[-(i+(j-1)*n), -(i+k*n)]]

    # no more than one "True" per diagonal
    # 17 18 19 20
    # 21 22 23 24
    # 25 26 27 28
    # 29 30 31 32 

    # 1. left top corner => right down
    # [[-17, -22], [-17, -27], [-17, -32], [-22, -27], [-22, -32], [-27, -32]]
    for i in range(0, n-1):        # 0, 1, 2
        for j in range(1, n-i):    # 1,2,3, 1,2, 1
            CNFs += [[-(m+1+i*(n+1)), -(m+1+i*(n+1)+j*(n+1))]]
    # 2. right top corner => left down
    # [[-20, -23], [-20, -26], [-20, -29], [-23, -26], [-23, -29], [-26, -29]]
    for i in range(0, n-1):        # 0, 1, 2
        for j in range(1, n-i):    # 1,2,3, 1,2, 1
            CNFs += [[-(m+n+i*(n-1)), -(m+n+i*(n-1)+j*(n-1))]]
    # 3. middle top => right down
    # [[-18, -23], [-18, -28], [-23, -28], [-19, -24]]
    for i in range(1, n-1):            # 1, 2
        for j in range(0, n-i-1):    # 0,1, 0
            for k in range(1, n-i-j):    # 1,2, 1
                CNFs += [[-(m+1+i+j*(n+1)), -(m+1+i+j*(n+1)+k*(n+1))]]
    # 4. middle top => left down
    # [[-19, -22], [-19, -25], [-22, -25], [-18, -21]]
    for i in range(1, n-1):            # 1, 2
        for j in range(0, n-i-1):    # 0,1, 0
            for k in range(1, n-i-j):    # 1,2, 1
                CNFs += [[-(m+n-i+j*(n-1)), -(m+n-i+j*(n-1)+k*(n-1))]]
    # 5. middle bottom => left up
    # [[-31, -26], [-31, -21], [-26, -21], [-30, -25]]
    for i in range(1, n-1):            # 1, 2
        for j in range(0, n-i-1):    # 0,1, 0
            for k in range(1, n-i-j):    # 1,2, 1
                CNFs += [[-(m+m-i-j*(n+1)), -(m+m-i-j*(n+1)-k*(n+1))]]
    # 6. middle bottom => right up
    # [[-30, -27], [-30, -24], [-27, -24], [-31, -28]]
    for i in range(1, n-1):            # 1, 2
        for j in range(0, n-i-1):    # 0,1, 0
            for k in range(1, n-i-j):    # 1,2, 1
                CNFs += [[-(m+m-n+1+i-j*(n-1)), -(m+m-n+1+i-j*(n-1)-k*(n-1))]]

    return CNFs

def print_nQueen(a_list, n):
    lines = []
    horizontalLine = ('-' * (n*2 + 1))
    print horizontalLine
    for i in range(0, n*n, n):
        rowLine = '|'
        for j in range(0, n):
            if a_list[n*n+i+j] > 0: 
                rowLine = rowLine + 'Q|'
            else:
                rowLine = rowLine + ' |'
        print rowLine
        print horizontalLine
    print " "

if __name__ == '__main__':
    
    for n in range(4 , 12): 
        nQueen_CNFs = get_nQueen_CNFs(n)
        nQueen_list = list(pycosat.itersolve(nQueen_CNFs))
        num_sol = len(nQueen_list)
        print 'the number of solutions for placing',n,'queens on an',n,'×',n,'board is',num_sol
    '''
    n = 5
    nQueen_CNFs = get_nQueen_CNFs(n)
    nQueen_list = list(pycosat.itersolve(nQueen_CNFs))
    for i in range(0, len(nQueen_list)):
        print i+1
        print_nQueen(nQueen_list[i], n)
    '''
    


