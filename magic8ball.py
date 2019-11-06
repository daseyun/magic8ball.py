from random import randint

print("Enter your question")
a = input()

if randint(0,9)%2 == 0:
    print("yes")
else:
    print("no")