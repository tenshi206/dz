n=int(input("введите число: "))
k=int(input("введите число: "))
s=0
for i in range (n,k+1):
    if i%2==0:
        s +=i
  print (f'{s}')
