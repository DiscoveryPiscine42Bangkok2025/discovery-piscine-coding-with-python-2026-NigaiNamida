from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1) 

    board2 = """\
....
.K\
"""
    checkmate(board2) 

    board3 = """\
Q....
.P...
.....
..B..
..R..\
"""
    checkmate(board3)

    board4 = """\
Q....
.....
..K..
..B..
..R..\
"""
    checkmate(board4)

if __name__ == "__main__":
    main()