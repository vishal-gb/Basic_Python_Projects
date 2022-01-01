a=1
import random
m=random.randint(1,100)
n=int(input("Enter a number:"))
while (n!=m):
    if (n>m):
        print("guess is high")
        n=int(input("guess another number:"))
        a=a+1
    else:
        print("guess is low")
        n=int(input("guess another number:"))
        a=a+1
else:
    print("you guessed it right in",a,"guesses")
