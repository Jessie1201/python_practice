def name_frequence():
    count_dict = {}
    with open('nameslist.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.strip("\n")
            # simply strip() also works for removing whitespaces and \n
            # line = line.strip()
            if line in count_dict:
                count_dict[line] += 1
            else:
                count_dict[line] = 1
            line = f.readline()
    return count_dict

if __name__=="__main__":
    print(name_frequence())