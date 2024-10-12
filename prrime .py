def prime(n):
    list =[]
    prime = [True for i in range(n+1)]
    p=2
    while(p*p <= n):
        if(prime[p] == True):
            for i in range(p*p,n+1,p):
                prime[i]=False
                
        p+=1
        
    for p in range(2, n+1):
        if prime[p]:
           list.append(p)
        
    return list    

n = int(input("Enter last number: "))
prime = prime(n)
lenght = len(prime)
print("There are",lenght,"number in this limit")
print("They are: ",prime)
                