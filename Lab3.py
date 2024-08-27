import random 
import msvcrt   #library to use getch

#Q1. Write a python program to find the sum of n natural numbers. 
print("Output Q1:")
n=int(input("Enter the no. of terms: "))
sum=0
for i in range(n+1):
    sum+=i
print(f"The sum of {n} natural numbers is: {sum}\n")

#Q2. Write a program to read integer from user. For all non negative integers i<n, print i^2.
print("Output Q2:")
user_input=int(input("Enter the integer: "))
print("Square: ",end="")
for i in range(user_input):
    if i<user_input:
        print(i**2,end='\t')

#Q3. Write a python program that prints all the numbers from 0 to 6 except 0 and 6 using 'continue' statement.
print("\n\nOutput Q3:")
for i in range(7):
    if(i==3 or i==6):
        continue
    else:
        print(i,end="\t")

#Q4. Write a python program to get the fibonacci series upto n terms. 
print("\n\nOutput Q4:")
n=int(input("Enter the no. of terms: "))
print("Fibonacci Series: ",end=" ")
first_int=0
next_int=1
for i in range(n+1):
    print(first_int, end=" ")
    third_int=first_int+next_int
    first_int=next_int
    next_int=third_int

#Q5. Write a python program to find those numbers which are divisible by 7 and multiple of 5 between 1500 and 2700 (both included).
print("\n\nOutput Q5:")
print("Numbers between 1500 and 2700 that are divisible by 7 and are multiple of 5: ",end=" ")
for i in range(1500,2701,5):
    if(i % 7 ==0):
        print(i,end=" ")

#Q6. Write a python program to guess a number between 1 t0 9. If user prompted right guess print" Well guessed!" otherwise promt to guess again.  
number=random.randint(0,9)
print("\n\nOutput Q6: ")
while True:
    print("Guess the number:", end=" ")
    guess_int=int(input("<< "))
    if(guess_int==number):
        print("Well Guessed !!")
        break
    else:
        print("Try Again !!")
    
#Q7. Write a python program to develop a rock paper scissor game, restart the game until the user press 'n' when the game ends.
print("\nOutput Q7:") 
isTrue=True
while isTrue:
    system_call=random.choice(['rock','paper','scissor'])
    your_call=input("Scissor:Paper:Rock:???:::")
    system_call=system_call.lower()
    your_call=your_call.lower()
    print(f"Your Call: {your_call}\t My Call: {system_call}\t Result: ",end="")
    if (system_call=='rock'and your_call=='paper') or (system_call=='paper' and your_call=='scissor') or (system_call=='scissor' and your_call=='rock'):
        print("You Won !!")
    elif (system_call==your_call):
        print("It's a draw !!")
    else:
        print("Oops ! you lost.")
    ch=msvcrt.getch().decode('utf-8')   #convert byte-type to string
    if ch=='n' or ch=='N':
        break

#Q8. Write a python program to create a multiplicatio table from 1 to 10 of a number. 
print("\nOutput Q8: ")
number=int(input("Enter the number:"))
print(f"Multiplication Table of {number} from 1 to 10:")
for i in range(1, 11):
    print(f"{number} X {i} = {number*i}")

        
#Q9. Write a python program that accepts a word from the user and reverses it:
print("\nOutput Q9:")
word=input("Enter the word: ")
print("The reversed word is: ",end="")
for i in range(len(word),0,-1):
    print(word[i-1],end="")
print("\n")

#Q10. Python program to construct pattern:
"""
*
**
***
****
*****
****
***
**
*
"""
print("\nOutput Q10: ")
for i in range(1,10):
    if i<5:
        for j in range(1,i+1):
            print("*",end="")
    else:
        for j in range(i,10):
            print("*",end="")
    print("")



