measurement = []
signal = ""
value = 0
aim = 0
depth = 0
horizontal = 0



with open('input.txt', "r") as f:
    for line in f:
        measurement.append(line.strip("\n"))
for x in measurement:
    for letter in x:
        if letter.isalpha():
            signal += letter
        elif letter.isnumeric():
            value = int(letter)
    if signal == "forward":
        horizontal += value
        depth += (value * aim)
    elif signal == "down":
        aim += value
    elif signal == "up":
        aim -= value
    distance = 0
    signal = ""
print(horizontal)
print(depth)