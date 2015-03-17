answer = 0
column = 8
while column >= 1:
    bit = int(input("Enter bit value: "))
    answer = answer+(column*bit)
    column = column/2
print("Decimal value is: {0}".format(answer))
