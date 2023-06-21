import random
import string

if __name__ == "__main__":
    for letter in "tukas":
        x = random.choice(string.ascii_letters)
        while letter != x:
            x = random.choice(string.ascii_letters)
        print(x)
