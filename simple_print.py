#here is the space for variables
one = 60
num = 500
name, hobbies = input("What is your name? "), input("What are your hobbies? ")
num1 = int(input("Now, give me one number: "))
num2 = int(input("Give me a second number: "))
num3 = int(input("Give me a number to convert to binary: "))
list = [1,2,3,4,5,6,7,8,9,0]

#the code starts here
import math
print("="* one)
print("| Your name is ",name.capitalize(),"and your hobbies are \n",hobbies)
print("| Your name is ",len(name),"characteres long")
if num1>num2:
    print("|",num1,"is the first number and is greater than ",num2)
else:
    print("|",num2," is the second number and is greater than ",num1)
print("| The 3rd number in binary is after 0b string: ",bin(num3))
#print ("The value of Pi is ",math.pi)
print("="* one)
