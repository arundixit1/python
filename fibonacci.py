def find_fib(n):

    if n==1:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)


#find_fib(10)
# a= int(input("enter number for square:"))
# result = lambda a: a * a
# print(result(a))

nums = [1,2,3,4,5,6,7]
even = list(filter(lambda x: x % 2 == 0,nums))
print(even)

a1 = list(map(lambda a:a+10,nums))
print(a1)