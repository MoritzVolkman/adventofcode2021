measurement = []
positive = [0 for a in range(12)]
number = [0 for b in range(12)]
gammabin = [0 for c in range(12)]
epsilonbin = [0 for d in range(12)]
powerconsumption = 0

#get the entries from the input file
with open('input.txt', "r") as f:
    measurement = [ line.strip() for line in f ]
#add one to the corresponding entry in the "positive" list for each positive bit
for x in measurement:
    for y in range(12):
        if x[y] == "1":
            positive[y] += 1
        number[y] += 1
#check if more than half of the entries of the bit were positive and if that is the case, adjust to 1, otherwise to 0
for z in range(12):
    gammabin[z] = positive[z]/number[z]
    if gammabin[z] >= 0.5:
        gammabin[z] = 1
    else:
        gammabin[z] = 0
#make epsilonbin the complement of gammabin by comparing it xor with 1
    epsilonbin[z] = gammabin[z] ^ 1

print(gammabin)
print(epsilonbin)

gamma = 0
epsilon = 0
#convert the bit lists to integer values
for bitg, bite in zip(gammabin,epsilonbin):
    gamma = (gamma << 1) | bitg
    epsilon = (epsilon << 1) | bite
print(gamma)
print(epsilon)
powerconsumption = gamma * epsilon
print("Power Consumption: ", powerconsumption)


