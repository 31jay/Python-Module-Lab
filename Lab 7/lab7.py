#Q1.
import lab7Modules.my_math as my_math
firstNum=50
secondNum=10
print(f'{firstNum}+{secondNum}={my_math.add(firstNum,secondNum)}')
print(f'{firstNum}-{secondNum}={my_math.sub(firstNum,secondNum)}')
print(f'{firstNum}*{secondNum}={my_math.mul(firstNum,secondNum)}')
print(f'{firstNum}/{secondNum}={my_math.div(firstNum,secondNum)}')

#Q2. 
import lab7Modules.shapes as shapes 
len=5
radius=7
print(f'Area of circle r={radius}={shapes.circle_area(radius)}')
print(f'Area of square length={len}={shapes.square_area(len)}')

#Q3. 
from math import sqrt , pow 
p=4
b=3
print(f'Perpendicular={p}, Base={b} then Hypotenous',sqrt(pow(p,2)+pow(b,2)))

#Q4. 
from math import factorial as fact
num=5
print(f'Factorial of {num}=',fact(num))

#Q5.
import random as rand
print("Random num (1-10):",rand.randint(1,10))

#Q6. 
from lab7Modules.utilities import *
word="Hello"
print(f'Reverse {word}=',reverse_string(word))
print(f'Capitalized {word}=',capitalize(word))

#Q7. 
import lab7Modules.module_a as mod_a
import lab7Modules.module_b as mod_b
print(mod_a.greet())
print(mod_b.greet())

#Q8.
import my_package.my_math as math, my_package.utilities as util
print('Sum of 3 and 5=',math.add(3,5))
print('Reverse of Hello is:',util.reverse_string('Hello'))

#Q9. 
import lab7Modules.my_math as m 
print('my_math.py is imported in here: ')
print('5-3=',m.sub(5,3))

#Q10.
import lab7Modules.my_math as test 

assert test.add(3,5)==9
assert test.sub(5,3)==2
assert test.mul(5,2)==10

"""
import unittest
class TestmyFunction(unittest.TestCase):
    def test(self):
        self.assertEqual(test.add(2,2),4)
        self.assertEqual(test.sub(2,2),0)
unittest.main()"""