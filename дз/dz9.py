a=int(input("введите степендию: " ))
b=int(input("введите расходы: " ))
n=int(input("прожить месяцев: " ))
s=0
for i in range (0,n):
    s+=(b-a)*n
    if n%2==0:
        print (f"s+=(b-a)*n*1.03")
    else:
        print (f"s+=(b-a)*n*1.05")
print (s)
   
    


