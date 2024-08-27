#Q1.
print("\n\nQ1:")
py_dict={'name':'Hari','age':29,'city':'Kathmandu'}
print(py_dict['age'])

#Q2.
print("\n\nQ2:")
py_dict['occupation']='Engineer'
if 'occupation' in py_dict:
    print("Added Successfully")
    print(py_dict['occupation'])

#Q3. 
print("\n\nQ3:")
py_dict['city']='Bhaktapur'
print(py_dict.get('city'))
py_dict.update({'city':'Kathmandu'})
print(py_dict.get('city'))

#Q4. 
print("\n\nQ4:")
# py_dict.pop('age');
# del py_dict['occupation'];
# print(py_dict.keys());
# py_dict.popitem();
# py_dict.clear()
# print(py_dict.keys())


#Q5. 
print("\n\nQ5:")
for x in py_dict:
    print(x)
    print(py_dict[x])

for x,y in py_dict.items():
    print(x+'::'+str(y))

#Q6. 
print("\n\nQ6:")
if 'email' not in py_dict:
    print("Key Not Found")

#Q7.
print("\n\nQ7:")
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
# dict3={**dict1,**dict2}
# dict3=dict({**dict1,**dict2})
dict3=dict1.copy()
dict3.update(dict2)
print(dict3.keys())
print(dict3.values())

#Q8.
print("\n\nQ8:")
my_dict=dict([('a',1),('b',2),('c',3),('e',5)])
print(my_dict.keys())
print(my_dict.values())

#Q9. 
print("\n\nQ9:")
x=py_dict.get('age')
if 'age' not in py_dict:
    print("Key Not found.")

#Q10. 
print("\n\nQ9:")
for x,y in py_dict.items():
    print(f"{x}::{y}")

dictA={'A':1,'B':1,'C':1,'D':2}
print(f"Keys with value 1 are:")
for x,y in dictA.items():
    if y==1:
        print(x,end=',')

#Q11. 
print("\n\nQ11:")
original_dict = {'b': 5, 'a': 11, 'c': 33}
sorted_dict=dict(sorted(original_dict.items(),key=lambda  item:item[0]))
print(sorted_dict.keys())
print(sorted_dict.values())

# Q12.
print("\n\nQ12:")
sorted_dict=dict(sorted(original_dict.items(),key=lambda  item:item[1]))
print(sorted_dict.keys())
print(sorted_dict.values())

#Q13.
print("\n\nQ13:")
d={'a':1,'b':2,'c':3}
rev={}
for x,y in d.items():
    rev[y]=x
print(rev.keys())
print(rev.values())
rev={v: k for k, v in d.items()}
print(d)
print(rev)
