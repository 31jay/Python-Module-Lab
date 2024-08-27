#Qn 1 
#print all the even numbers from 1 to 10.
for i in range(1,10): 
    if i%2==0:
        print (i)

#Qn: 2
'''
#2 Add logic to print two lines. 
The first line should contain the result of integer division //.
The second line should contain the result of float division. 
'''
a=int(input("First Number: "))
b=int(input("Second Number: "))
# print(a/b)
# print(a//b)
print("The integer division is:",(a//b))
print("The float division i: ",(a/b))    

#Qn 3 Evaluate:
#a. 4*(6+5)
print(4*(6+5))
#b. 4*6+5
print(4*6+5)
#c. 4+6*5
print(4+6*5)
#d. (5>4) and (5==5)
print((5>4)and (5==5))
#e. not (5>4)
print(not (5>4))
#f. (5>4) or (3==5)
print((5>4) or (3==5))
#g. not ((5>4)or(3==5))
print(not ((5>4)or(3==5)))
#h. (True and True)and(True ==False)
print((True and True)and(True ==False))
#i. (not False) or (not True)
print((not False) or (not True))

#Qn 4. What is the type of the result of the expression 3*1.5+4
print(type(3*1.5+4))

#Qn 5. Find the numbers square root and square
number=4
print("The square root is",4**0.5)
print("The square is:",4**2)

#Qn 6. Take an input from user then reverse the string using slicing:
user_string=str(input("Enter String:"))
print("Reversed String is:",user_string[::-1])

#Qn 7. Write code to input from user and store it in variavle spam and then print Hello if 1 is stored in spam, print Hi, if 2 is stored in spam ad print Greetings! if anything else is stored in spam.
user_input=int(input("Prompt Number:"))
if user_input==1:
    print("Hello")
elif user_input==2:
    print("Hi")
else:
    print("Greetings !")

#Qn 8. Write a python script that takes two numbers as input and print their sum, difference, product and quotient using match case.
num_1=int(input("First Number:"))
num_2=int(input("Second Number:"))
operator=input("Operation: ")
match operator:
    case '+':
        print("The sum is: ", num_1 + num_2)
    case '-':
        print("The difference is:", num_1-num_2 )
    case '*':
        print("The product is:", num_1*num_2 )
    case '/':
        print("The float division is:", num_1/num_2 )   
    case '//':
        print("The quotient is:", num_1//num_2 ) 
    case _:
        print("Invalid operation !!")
    
#Qn 9. Write a script that asks a user for the name and age, then prints a message that tells them the year in which they will turn 100 years old.
stringName=str(input("Enter your Name:"))
stringAge=int(input("Enter your Age:"))
print("Hello",stringName,"!! You will be 100 years old in",2023+(100-stringAge))

# Qn 10. Create a python script that converts temperature from Fahrenheit to Celcius and viceversa.
temperature=int(input("Input Temperature:"))
stringUnit=str(input("Temp. Degree ?? (C/F):"))
if(stringUnit=='C'or stringUnit=='c'):
    print("In Farenheit, it Equals:",(9/5*temperature)+32,"degree.")
elif(stringUnit=='F'or stringUnit=='f'):
    print("In Celcius. it is Equals:",(temperature-32)*5/9,"degree.")
else:
    print("Invalid Conversion !!")

#Qn 11. Create a program that asks for a age and prints "Child" if the age is less than 12, "Teenager" if age is between 13 and 19 and "Adult" for ages 20 and above.

string_age=int(input("Enter your age:"))
if string_age<=12:
    print("You are Child !")
elif string_age>=13 and string_age<=19:
    print("You are a teenager !")
elif string_age>=20:
    print("You are an adult !")
else:
    print("Something went wrong !")

#Qn 12. Write a python script that takes a letter grade (A,B,C,D,F) as input and prints the corresponding grade point average (GPA). Eg. A=4.0, B=3.0, C=2.0, D=1.0, F=0.0. Include an else statement to handle invalid inputs.
stringGrade=str(input("Enter the grade: "))
if stringGrade=='A' or stringGrade=='a':
    print("Equivalent Grade Point (GP)= 4.0")
elif stringGrade=='B' or stringGrade=='b':
    print("Equivalent Grade Point (GP)= 3.0")
elif stringGrade=='C' or stringGrade=='c':
    print("Equivalent Grade Point (GP)= 2.0")
elif stringGrade=='D' or stringGrade=='d':
    print("Equivalent Grade Point (GP)= 1.0")
elif stringGrade=='F' or stringGrade=='f':
    print("Equivalent Grade Point (GP)= 0.0")
else:
    print("Invalid Grade Entered !!")

#Qn 13. Wtrite a python program that takes a number and print whether it is "Even", "Odd", "Zero" or "Invalid" for non-integer inputs. This program should first check if the input is valid integer and then only check for other conditions.
numberInput=input("Enter the number")
if numberInput.isdigit:
    calcValue=int(numberInput)
    if(calcValue%2==0):
        print("It is even number")
    elif(calcValue%2!=0):
        print("It is odd number")
    else:
        print("It is zero !")
else:
    print("It is not a valid integer !!")

# Qn 14. . An extra day is added to the calendar almost every four years as February 29, and the thay is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day. In the Gregorian calendar, three conditions are used to identify leap years
# • The year can be evenly divided by 4, is a leap year, unless
# • The year can be evenly divided by 100, it is not a leap year, tunless:
# • The year is also evenly divisible by 400. Then it is a leap year
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are not leap years.
year=int(input("Enter the year: "))
print("Leap Year Check ",end=":")
if ((year%4==0)):
    if(year%100==0):
        if(year%400==0):
            print("It is a leap year")
        else:
            print("It is not leap year")
    else:
        print("It is a leap Year")
else:
    print("It is not leap Year")

