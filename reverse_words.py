def backwards():
        org = str(input("a sentences: "))
        split_li = org.split()
        reverse_li = []
        while len(split_li) > 0:
                reverse_li.append(split_li[-1])
                split_li = split_li[:-1]
        result = " ".join(reverse_li)
        print(result)

backwards()