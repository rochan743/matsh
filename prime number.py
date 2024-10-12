from math import sqrt

n = int(input("Enter a number: "))

isPrime = False

if n>1:
    for i in range(2 , int(sqrt(n))*1):
        if(n % i) == 0:
            isPrime = False
            break
        else:
            isPrime = True
    if(isPrime):
        print(n, "Is a prime number")
    else:
        print("Not a prime number")            