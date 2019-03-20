def num_in_list(num, ordered_list):
    new_list = ordered_list
    while len(new_list) > 1:
        mid = new_list[int(len(new_list)/2)]
        if num >= mid:
            new_list = new_list[int(len(new_list)/2):]
        else:
            new_list = new_list[:int(len(new_list)/2)]
    if new_list[0] == num:
        belong = 1
    else:
        belong = 0
    return belong

if __name__=="__main__":
    print(num_in_list(8, [1,2,3,4,5,6,7]))