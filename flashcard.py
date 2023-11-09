import random
import os
with open("words.list.txt", "r") as f:
    lines = f.read().split("==")
    list = random.sample(range(0, len(lines)-1), len(lines)-1)

    for index in list:
        line = lines[index]
        words = line.split("=>")
        s = 0
        while True:
            print(words[s])
            data = input("\n")
            os.system('cls||clear')
            if not data:
                s = 1-s
            else:
                break


# import random
# data = list(range(numLow, numHigh))
# random.shuffle(data)
# print data
