#Q1. 
def greet():
    print('Hello world !')

greet()

#Q2. 
def factorial(num):
    if(num==0):
        return 1
    else:
        # fact=1
        # while(num>0):
        #     fact=fact*num
        #     num=num-1
        return num*factorial(num-1)
    
print("0 factorial:", factorial(0))
print("5 factorial:", factorial(5))

#Q3.
def area_rect(len,wid):
    return len*wid
print('The area of rectaanle (l=10 and b=5):',area_rect(10,5))

#Q4.
def area_rect(len=1,wid=1):
    return len*wid
print('The area of rectaanle (default len and width: 1):',area_rect())

#Q5. 
def ret_dict(name, age):
    return dict([(name,age)])

print('My dict:',ret_dict('H.Ad.',100))

#Q6.
def sum_list(myList):
    # sum=0
    # for items in myList:
    #     sum=sum+items
    return sum(myList)
list1=[1,1,1,1,1]
print(f"Sum of list {list1} is:",sum_list(list1))

#Q7. 
def intro(name,roll):
    print(f'{name}s Roll is: {roll}')
intro('H. Ad.',33)          #This is positional(Functional) argument since arguments are passed based on the position of parameters.
intro(roll=33,name='H. Ad.') # This is keyword arguments since arguments order is not considered and passed with reference to the parameter name. 

#Q8.
def app_list(myList, num):
    myList.append(num)
    return myList
list1=[1,2,3,4]
print('Appended List: (5 is added)',app_list(list1,5))

#Q9:
def doubled_list(myList):
    doubledList=[elem*2 for elem in myList]
    return doubledList
list1=[2,3,4,5]
print('Doubled List:',doubled_list(list1))

#Q10.
def calculate_average(myList):
    return sum(myList)/len(myList)
print(f"Average of list {list1}:", calculate_average(list1))

#Q11.
def un_changed(myList, num):
    myList.append(num)
    return myList
list1=[1,2,3,4]
print(f"Appened 5 in {list1}:",un_changed(list1[:],5))
print(f"Unchanged List1 :{list1}")

#Q12.
def pali_check(str):
    return (str[::-1].lower()==str.lower())
print("Is Hello Palindrom:",pali_check('Hello'))
print("Is Radar Palindrome:",pali_check('Radar'))
