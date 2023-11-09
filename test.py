with open("words.list.txt", "r") as f:
    lines = f.read().split("==")

[print(line) for line in lines]