# calculate how many numbers are even and how many are odd
finished = False
even = odd = 0
while (not finished):
    n = int(input("Enter a number or zero to end the program: "))
    if n == 0:
        finished = True
    else:
        if n % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

print ("Even = ", even)
print ("Odd = ", odd)