n=int(input("enter a number:"))
count=0
i=2
while(i<=n//2):
    if(n%i==0):
        count=count+1
        break
    i=i+1
if(count==0 and n!=1):
    print("prime number:")
else:
    print("number is not prime")
                