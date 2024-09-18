x=int(input("введите число: "))
n=int(input("введите число: "))
s=0
for i in range (1,n+1):
    s+=1/(x**(2*i -2))
    print (s)
