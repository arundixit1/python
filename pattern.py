def righttr(n):
    for x in range(n):
        for y in range(x):
            print('* ', end ='')
        print(" ")


def pyramid(n):
    k = 2 * n -2
    for x in range(n):
        for y in range(k):
            print(end =' ')
        k = k -1
        for z in range(x+1):
            print("x ",end='')
        print("\r")


#righttr(4)
pyramid(3)
