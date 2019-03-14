import random
import string

def cows_and_bulls():
    secret = ''.join(random.choice(string.digits) for i in range(4))
    cows = 0
    while cows < 4:
        cows = 0
        bulls = 0
        usr_num = str(input("Give a 4-digit number: "))
        for el in usr_num:
            if el in secret:
                if usr_num.index(el) == secret.index(el):
                    cows += 1
                else:
                    bulls += 1
        print(str(cows) + "cows " + str(bulls) + "bulls")
        print(secret)

if __name__=="__main__":
    cows_and_bulls()