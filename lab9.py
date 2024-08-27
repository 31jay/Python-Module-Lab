# 1. Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen
'''f=open("poem.txt",'r')
for x in f:
    print(x,end="")
'''
# 2. Write a Python program to read first n lines of a file.
'''f=open("poem.txt",'r')
count=4
for x in f:
    print(x,end="")
    count-=1
    if(count==0):
        break'''
# 3. Write a Python program to count the number of lines in a text file which starts with an alphabet "T".
'''f=open('poem.txt','r')
count=0
for x in f:
    if x.startswith('B'):
        count+=1
print(count)'''

# 4. Write a Python program to append text to a file and display the text.
'''f=open('myfile.txt','a+')
f.write('This is appended.')
f.seek(0)
print(f.read())'''

# 5. Write a Python program to read a file line by line and store it into a list.
'''f=open('myfile.txt','r')
strList=[x for x in f]
print(strList[1])'''

# 6. Write a Python program to read a file line by line store it into a variable. 
'''f=open('myfile.txt','r')
str=''
for x in f:
    str+=x
print(str)'''

# 7. Write a Python program to read a file line by line store it into an array.

# 8. Write a Python program to count and display the total number of words in a file.
'''f=open('myfile.txt','r')
str=''
wordcount=0
spacecount=0
for x in f:
    str+=x.strip()
for letters in str:
    if letters != " ":
        wordcount+=1
    else:
        spacecount+=1
print('Total Letters:',wordcount)
print('Total Space',spacecount)'''

# 9. Write a function in Python to read lines from a text file "poem.txt". Your function should find and display the occurrence of the word "the".
'''f=open('poem.txt','r')
str=[]
count=0
for x in f:
    x=x.strip()
    x=x.strip(',')
    x=x.strip('.')
    str.extend(x.split(' '))

for word in str:
    if word.lower()=='the':
        count+=1
print(count)'''

# 10. Write a Python program to write a list to a file.
'''list=['Hello','Wriring','To','File']
f=open('write.txt','w')
for items in list:
    f.write(items+' ')
'''
# 11. Write a Python program to copy the contents of a file to another file.
'''source=open('poem.txt','r')
destination=open('poem_copy.txt','w')
destination.write(source.read())'''

# 12. Write a Python program to read a random line from a file.
'''import random as rd 
f=open('poem.txt','r')
lines=f.readlines()
lineNo=rd.randint(0,len(lines)-1)
print(lines[lineNo])'''

# 13. Write a Python program to remove newline characters from a file.


# 14. Write a Python program to extract characters from various text files and puts them into a list.
# 15. Ram has used a text editing software to type some text. After saving the article as WORDS.TXT, she realised that she has wrongly typed alphabet J in place of alphabet I everywhere in the article.
# Write a function definition for IOI() in Python that would display the corrected version of entire content of the file WORDS.TXT with all the alphabets "J" to be displayed as an alphabet "I" on screen.
# Note. Assuming that WORD. TXT does not contain any Jalphabet otherwise.
# 16. Demostrate Renaming, Moving. Copying, and Removing operations of Files in python with or without shutil package.