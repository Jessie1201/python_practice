def find_overlap():
    prime_li = []
    with open('primenumbers.txt', 'r') as f_prime:
        line = f_prime.readline()
        while line:
            prime_li.append(line.strip())
            line = f_prime.readline()

    happy_li = []
    with open('happynumbers.txt', 'r') as f_happy:
        line = f_happy.readline()
        while line:
            happy_li.append(line.strip())
            line = f_happy.readline()

    overlap = []
    for el in prime_li:
        if el in happy_li:
            overlap.append(el)
    return overlap


if __name__=="__main__":
    print(find_overlap())