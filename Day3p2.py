measurement = []

#get the entries from the input file
with open('input.txt', "r") as f:
    measurement = [ line.strip() for line in f ]

def findRating(bitToSearch):
    positive = [0 for a in range(12)]
    number = [0 for b in range(12)]
    blacklist = []
    rating = [0 for c in range(12)]

    for y in range(12):
        for x in measurement:
            if not (x in blacklist):
                if x[y] == "1":
                    positive[y] += 1
                number[y] += 1
        if bitToSearch:
            if (positive[y]/number[y]) >= 0.5:
                rating[y] = 1
                for z in measurement:
                    if z[y] == "0":
                        blacklist.append(z)
            else:
                rating[y] = 0
                for z in measurement:
                    if z[y] == "1":
                        blacklist.append(z)
        else:
            if not number[y] <= 1:
                if (positive[y]/number[y]) >= 0.5:
                    rating[y] = 0
                    for z in measurement:
                        if z[y] == "1":
                            blacklist.append(z)
                else:
                    rating[y] = 1
                    for z in measurement:
                        if z[y] == "0":
                            blacklist.append(z)
            else:
                rating[y] = positive[y]
    intrating = 0
    for bit in rating:
        intrating = (intrating << 1) | bit
    return intrating
    
print("Oxygen Rating:", findRating(1))
print("CO2 Rating:", findRating(0))
print("Life Support Rating:", findRating(1) * findRating(0))








