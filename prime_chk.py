# num = int(input("input number to test prime"))
# for i in range(2,num):
#     if num%i ==0:
#         print("not prime")
#         break
# else:
#     print("its prime")
j=10000000000000000
z=0
while j<10000000000000000000:
    for i in range(2,j):
        if j%i ==0:
            break
    else:
        print(j)
        z+=1
    j+=1
print("total prime numbers are :"+ str(z))