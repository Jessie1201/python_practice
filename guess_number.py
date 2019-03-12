import random
goal = random.randint(1, 9)
count = 0

result = "false"

while result == "false":
    org = input("a integer from 1 to 9: ")
    count += 1
    if org == "exit":
        result = "stop"
    else:
        guess = int(org)
        if guess == goal:
            print("Got it " + str(count))
            result = "true"
        elif guess > goal:
            print("smaller")
        elif guess < goal:
            print("bigger")

