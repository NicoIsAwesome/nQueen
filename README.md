# nQueen

## nQueen wiki page
https://en.wikipedia.org/wiki/Eight_queens_puzzle

## Requirements
pip install pycosat

## Usage (python2 only)
python nQueens.py

## [1] print out the number of solutions 
```
   for n in range(4 , 12): 
        nQueen_CNFs = get_nQueen_CNFs(n)
        nQueen_list = list(pycosat.itersolve(nQueen_CNFs))
        num_sol = len(nQueen_list)
        print 'the number of solutions for placing',n,'queens on an',n,'×',n,'board is',num_sol
```
results:
```
the number of solutions for placing 4 queens on an 4 × 4 board is 2
the number of solutions for placing 5 queens on an 5 × 5 board is 10
the number of solutions for placing 6 queens on an 6 × 6 board is 4
the number of solutions for placing 7 queens on an 7 × 7 board is 40
the number of solutions for placing 8 queens on an 8 × 8 board is 92
the number of solutions for placing 9 queens on an 9 × 9 board is 352
the number of solutions for placing 10 queens on an 10 × 10 board is 724
the number of solutions for placing 11 queens on an 11 × 11 board is 2680
```

## [2] print out all solutions 
```
    n = 5
    nQueen_CNFs = get_nQueen_CNFs(n)
    nQueen_list = list(pycosat.itersolve(nQueen_CNFs))
    for i in range(0, len(nQueen_list)):
        print i+1
        print_nQueen(nQueen_list[i], n)
```
results:
```
1
-----------
|Q| | | | |
-----------
| | |Q| | |
-----------
| | | | |Q|
-----------
| |Q| | | |
-----------
| | | |Q| |
-----------
 
2
-----------
|Q| | | | |
-----------
| | | |Q| |
-----------
| |Q| | | |
-----------
| | | | |Q|
-----------
| | |Q| | |
-----------
 
3
-----------
| |Q| | | |
-----------
| | | |Q| |
-----------
|Q| | | | |
-----------
| | |Q| | |
-----------
| | | | |Q|
-----------
 
4
-----------
| |Q| | | |
-----------
| | | | |Q|
-----------
| | |Q| | |
-----------
|Q| | | | |
-----------
| | | |Q| |
-----------
 
5
-----------
| | | | |Q|
-----------
| | |Q| | |
-----------
|Q| | | | |
-----------
| | | |Q| |
-----------
| |Q| | | |
-----------
 
6
-----------
| | | | |Q|
-----------
| |Q| | | |
-----------
| | | |Q| |
-----------
|Q| | | | |
-----------
| | |Q| | |
-----------
 
7
-----------
| | | |Q| |
-----------
|Q| | | | |
-----------
| | |Q| | |
-----------
| | | | |Q|
-----------
| |Q| | | |
-----------
 
8
-----------
| | | |Q| |
-----------
| |Q| | | |
-----------
| | | | |Q|
-----------
| | |Q| | |
-----------
|Q| | | | |
-----------
 
9
-----------
| | |Q| | |
-----------
| | | | |Q|
-----------
| |Q| | | |
-----------
| | | |Q| |
-----------
|Q| | | | |
-----------
 
10
-----------
| | |Q| | |
-----------
|Q| | | | |
-----------
| | | |Q| |
-----------
| |Q| | | |
-----------
| | | | |Q|
-----------
```
