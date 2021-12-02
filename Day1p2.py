measurement = []
counter = 0


f = open('input.txt', "r")
for line in f:
    measurement.append(int(line.strip("\n"))) 
for x in range(len(measurement)):
    if x >= 3:
        sum1 = measurement[(x-3)] + measurement[(x-2)] + measurement[(x-1)]
        sum2 = measurement[(x-2)] + measurement[(x-1)] + measurement[x]
        if sum2 > sum1:
            counter = counter + 1
    else:
        print("noch nicht genuegend Daten")

print(counter)