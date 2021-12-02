measurement = []
lastmeasurement = 0
counter = 0

f = open('input.txt', "r")
for line in f:
    measurement.append(int(line.strip("\n"))) 
for x in measurement:
    if x > lastmeasurement and lastmeasurement != 0:
        counter = counter + 1
    lastmeasurement = x
print(counter)

