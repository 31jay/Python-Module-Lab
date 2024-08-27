# #Q1. Write a python program to print the items in a list. 
# my_list=['cricket','football','chess','shooting','boxing']
# print(my_list)      #displays all the list
# print(my_list[0])   #prints first item only
# for i in range(len(my_list)):   #displays all items by looping 
#     print(my_list[i],end=", ")

# #Q2. Use range function to print all the even numbers from 1 to 10.
# print("Even Numbers from 1 to 10")
# for i in range(1,11,2):     #displays the numbers leaving odd. 
#     print(i, end=",")

# #Q3. Write a program to print largest item in a list without using buit-in functions: 
# my_list=[1,2,3,4,5,6,7,8,9,15]
# largest=my_list[0]
# for i in range(len(my_list)):
#     if(largest<my_list[i]):
#         largest=my_list[i]
# print(f"Largest Number is: {largest}")

# #Q4. Write a python program to print a specified list after removing 0th, 4th and 5th element. 
# my_list=['cricket','football','chess','shooting','boxing','swimming','tennis']
# print(f"Original List: {my_list}")
# my_list.pop(0)                  #removes indexed item
# my_list.remove('boxing')        #removes passed element;
# my_list.pop(3)
# print(f"Final List: {my_list}")

# #Q5. Write a python program to check if all the numbers in the list are prime. Return true of all the elements are true else print false. 
# def checkList(input_list):
#     for num in input_list:
#         factor = 0
#         if num == 1:
#             factor += 1
#         else:
#             for j in range(1, num + 1):
#                 if num % j == 0:
#                     factor += 1
#         if factor > 2:
#             status = False
#             break
#         else:
#             status = True
#     print(f"{input_list}: {status}")
# num_list = [2, 4, 6, 8, 10, 12, 15]
# prime_list = [2, 3, 5, 7, 11, 13]
# checkList(num_list)         #displays False
# checkList(prime_list)       #displays True

# #Q6. Write a python program to combine two lists and remove all duplicates from the list: 
# list1=[1,2,3,4,5,6,7,8]
# list2=[4,5,6,7,8,9]
# combined=list1+list2
# unique=list(set(combined))
# print(unique)

# #Q7. Write a python program to print the list in reverse order. 
# list1=[1,2,3,4,5]
# reversedList=list1[::-1]
# print(reversedList)

#Q8. Write a python program to sort given list of string(numbers) numerically. 
# string_numbers = ["10", "5", "22", "7", "15"]

# print("Original List:", string_numbers)

# # Sort the list numerically
# sorted_numbers = sorted(map(int, string_numbers))

# print("Sorted List Numerically:", sorted_numbers)

# #Q9. Apply functions like: append, remove, pop, insert, sort, max, min in a list. 
# my_list=[1,2,3,5,6,7,8,9,15,20]
# list.append(100)
# print("After Append (100): ", my_list)
# list.append(2,111)
# print("Append (2,111): ",my_list)
# list.remove(100)
# print("After Removing 100: ", my_list)
# list.insert()
# Example list
# my_list = [10, 5, 8, 12, 3]

# # Append: Add an element to the end of the list
# my_list.append(15)

# # Remove: Remove the first occurrence of a value
# my_list.remove(8)

# # Pop: Remove and return an element by index (default is the last element)
# popped_element = my_list.pop(2)

# # Insert: Insert a value at a specific index
# my_list.insert(1, 20)

# # Sort: Sort the list in ascending order
# my_list.sort()

# # Max: Find the maximum value in the list
# max_value = max(my_list)

# # Min: Find the minimum value in the list
# min_value = min(my_list)

# # Print the modified list and results
# print("Modified List:", my_list)
# print("Popped Element:", popped_element)
# print("Max Value:", max_value)
# print("Min Value:", min_value)


# #Q10. Write a python program to sort a list of lists by a given index of the inner list. 
# my_list=[[1,4,2,3,7],[12,10,5,-3,0,1],[5,3,9,0,-2,-4]]
def sort_list_of_lists(list_of_lists, index_to_sort):
    """
    Sorts a list of lists by a given index of the inner list.

    Parameters:
    - list_of_lists (list): The list of lists to be sorted.
    - index_to_sort (int): The index of the inner list to use for sorting.

    Returns:
    - Sorted list of lists.
    """
    sorted_list = sorted(list_of_lists, key=lambda x: x[index_to_sort])
    return sorted_list

# Example usage:
list_of_lists = [[3, 7, 2], [1, 5, 4], [6, 8, 0]]
index_to_sort = 1

sorted_list_of_lists = sort_list_of_lists(list_of_lists, index_to_sort)

print("Original List of Lists:", list_of_lists)
print(f"Sorted List of Lists by Index {index_to_sort}:", sorted_list_of_lists)


