# Define two example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print("Original Lists:")
print("list1:", list1)
print("list2:", list2)
print("-" * 40)

# 1. Append (add one element to end of list1)
list1.append(6)
print("After list1.append(6):", list1)

# 2. Extend (add all elements from list2 to list1)
list1.extend(list2)
print("After list1.extend(list2):", list1)

# 3. Insert (insert element at specific position in list2)
list2.insert(2, 99)
print("After list2.insert(2, 99):", list2)

# 4. Remove (remove first occurrence of element from list1)
list1.remove(3)
print("After list1.remove(3):", list1)

# 5. Pop (remove and return last element from list2)
popped_element = list2.pop()
print(f"After list2.pop(): {list2}, popped element: {popped_element}")

# 6. Clear (remove all elements from a list)
temp_list = list1.copy()
temp_list.clear()
print("After temp_list.clear():", temp_list)

# 7. Index (find index of first occurrence of an element)
index_4_in_list1 = list1.index(4)
print("Index of 4 in list1:", index_4_in_list1)

# 8. Count (count how many times an element appears)
count_5_in_list1 = list1.count(5)
print("Count of 5 in list1:", count_5_in_list1)

# 9. Sort (sort list2 in ascending order)
list2.sort()
print("After list2.sort():", list2)

# 10. Reverse (reverse list1 in place)
list1.reverse()
print("After list1.reverse():", list1)

# 11. Copy (create a shallow copy)
list3 = list1.copy()
print("Copy of list1 (list3):", list3)

# 12. Using built-in functions on lists

# len() - length of list
print("Length of list1:", len(list1))

# sum() - sum of elements (only if elements are numbers)
print("Sum of list1 elements:", sum(list1))

# max() and min()
print("Max element in list1:", max(list1))
print("Min element in list1:", min(list1))

# 13. List comprehension - intersection of two lists
intersection = [x for x in list1 if x in list2]
print("Intersection of list1 and list2:", intersection)

# 14. List comprehension - union of two lists (unique elements)
union = list(set(list1) | set(list2))
print("Union of list1 and list2:", union)

# 15. Concatenation using '+' operator
concat = list1 + list2
print("Concatenation of list1 and list2:", concat)

# 16. Multiplication - repeat list elements
multiplied_list = list1 * 2
print("list1 repeated twice:", multiplied_list)

# 17. Membership test using 'in'
print("Is 4 in list2?", 4 in list2)
print("Is 100 in list1?", 100 in list1)

# 18. Slicing
print("list1 slice [1:5]:", list1[1:5])
print("list2 slice [::2] (every second element):", list2[::2])

# 19. Enumerate example
print("Enumerate list1:")
for idx, val in enumerate(list1):
    print(f"Index {idx}: Value {val}")

# 20. Sorting with custom key (sort by negative value to get descending)
list2.sort(key=lambda x: -x)
print("list2 sorted descending:", list2)
