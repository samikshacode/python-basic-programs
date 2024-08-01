def add(first_number,second_number):
    return first_number+second_number

def substract(first_number,second_number):
    return first_number-second_number

def multiply(first_number,second_number):
    return first_number*second_number

def division(first_number,second_number):
    return first_number/second_number

def modulus(first_number,second_number):
    return first_number%second_number


print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.division")
print("5.Modulus")
choice=input("Enter the choice[1/2/3/4/5]:")
number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))


if choice=="1":
   print(number1 ,"+", number2, "=", add(number1,number2))

elif choice=="2":
   print(number1 ,"-", number2, "=", substract(number1,number2))

elif choice=="3":
   print(number1 ,"*", number2, "=",multiply(number1,number2))

elif choice=="4":
   print(number1 ,"/", number2, "=", division(number1,number2))

elif choice=="5":
   print(number1 ,"%", number2, "=", modulus(number1,number2))

else:
    print("Invalid choice!")
