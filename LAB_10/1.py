import numpy as np
def Queens(n):
    board = np.array([["." for i in range(n)] for i  in range(n)])
    board = board.tolist()
    col = set()
    posdiag = set()
    negdiag = set()
    res = []
    def backtrack(r):
        if r == n:
            res.append([row[:] for row in board ]) # append each successful arrangement of queens
            return
        for c in range(n):
            if c in col or (r+c) in posdiag or (r-c) in negdiag:
                continue # skip blocks that are not safe

            col.add(c)
            posdiag.add(r+c)
            negdiag.add(r-c)
            board[r][c] = "Q" # insert queen at safe block
            
            backtrack(r+1)  
            
            col.remove(c)
            posdiag.remove(r+c)
            negdiag.remove(r-c)
            board[r][c] = "."  # remove last inserted queen to check for further possible arrangements

    backtrack(0)
    res = np.array(res)
    return res
ways = {1:1,
2:0,
3:0,
4:2,
5:10,
6:4,
7:40,
8:92,
9:352,
10:724}
N = int(input("Enter size of chess board "))
print(f"Total ways = {ways[N]} for {N}x{N}  chess board")
print(Queens(N))