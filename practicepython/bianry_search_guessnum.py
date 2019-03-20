def guess_search():
    usr_num = int(input("Give a number 0 - 100: "))
    li = list(range(0, 101))
    count = 0
    correct = 0
    while correct == 0:
        guess = li[int(len(li)/2)]
        count += 1
        if usr_num == guess:
            correct = 1
        elif usr_num >= guess:
            li = li[int(len(li)/2):]
        else:
            li = li[:int(len(li)/2)]
    return "Python got it after guessing " + str(count) + " time(s)"

if __name__=="__main__":
    print(guess_search())