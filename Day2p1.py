measurement = []
signal = ""
distance = 0
depth = 0
horizontal = 0



with open('input.txt', "r") as f:
    for line in f:
        measurement.append(line.strip("\n"))
for x in measurement:
    for letter in x:
        if letter.isalpha():
            signal += letter
            print(signal)
        elif letter.isnumeric():
            distance = int(letter)
            print(distance)
        else:
            print(" ")
    if signal == "forward":
        horizontal += distance
    elif signal == "down":
        depth += distance
    elif signal == "up":
        depth -= distance
    distance = 0
    signal = ""
print(horizontal)
print(depth)