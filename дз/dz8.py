s=0

for i in range(int(1e6)):
    a=int(i%10)
    b=int((i%100)//10)
    c=int((i%1000)//100)

    d=int((i//10**3)%10)
    e=int((i//10**4)%10)
    f=int((i//10**5)%10)

    s1=d+e+f
    s2=a+b+c

    if s1==13 and s2==13:
        s+=1
print (f"{s}")
    

    
