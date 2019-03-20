# Srong, 8-character: lowercase, uppercase, numbers, and symbols. 
# Weak, 8-character: only numbers
import random
import string

def generate_pin():
    pin = ""
    strong = str(input("Want a strong password, y/n? "))
    if strong == "n":
        for i in range(8):
            pin += str(random.randint(0,9))
    elif strong == "y":
        for i in range(8):
            pin += str(random.choice(
                string.ascii_uppercase + 
                string.ascii_lowercase + 
                string.digits + 
                string.punctuation))
    print("Your pin is: " + pin)


generate_pin()