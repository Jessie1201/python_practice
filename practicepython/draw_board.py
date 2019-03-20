def draw_board():
    n = int(input("Now you want a board of n * n. Your n: "))
    head = " " + "--- " * n
    body = "|" + "   |" * n
    board = head + ("\n" +
                    body + "\n" +
                    head) * n
    return board

if __name__=="__main__":
    print(draw_board())