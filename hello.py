print("hello world")
name = 'Arun'
print('{0} is my name'.format(name))
print (name + ' is my name')
print('{0:.11f}'.format(1.0/3))
print('a',end='')
print('b')
i=5;print(i*2)
number =10
running =True
while running:
    guess = int(input("guess an integer:"))
    if guess == number:
        print("you guessed right")
        running = False
    elif guess < number:
        print("you guessed lower number")
    else:
        print("you guessed highter number")
print("done")

