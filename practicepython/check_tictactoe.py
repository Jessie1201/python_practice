def check_winner(state):
    winner = "no winner"
    for row in state:
        if row[0] == row[1] == row[2]:
            winner = row[0]
    for i in range(3):
        if state[0][i] == state[1][i] == state[2][i]:
            winner = state[0][i]
    if state[0][0] == state[1][1] == state[2][2]:
        winner = state[0][0]
    elif state[0][2] == state[1][1] == state[2][0]:
        winner = state[0][2]
    return winner

if __name__=="__main__":
    print(check_winner([[2, 2, 0],
                        [2, 1, 0],
                        [2, 1, 1]]))
    print(check_winner([[1, 2, 0],
                        [2, 1, 0],
                        [2, 1, 1]]))
    print(check_winner([[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]))
    print(check_winner([[1, 2, 0],
                        [2, 1, 0],
                        [2, 1, 2]]))