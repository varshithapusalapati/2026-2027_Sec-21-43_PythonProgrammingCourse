num=int(input("enter a number"))
orig_num=num
total=0
while num>0:
    digit=num%10
    total=total+digit**3
    num=num//10
if total == orig_num:
    print(f"{orig_num} is an armstong number")
else:
    print(f"{orig_num}is not a armstong number")