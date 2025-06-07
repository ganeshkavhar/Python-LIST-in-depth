# list_comprehension_examples.py

# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print("Original Lists:")
print("list1:", list1)
print("list2:", list2)
print("-" * 40)

# 1. Simple transformation — square each element in list1
squares = [x**2 for x in list1]
print("1. Squares:", squares)

# 2. Filtering — elements greater than 3 in list2
greater_than_3 = [x for x in list2 if x > 3]
print("2. Elements > 3:", greater_than_3)

# 3. Combine transformation and filtering — squares of even numbers in list1
even_squares = [x**2 for x in list1 if x % 2 == 0]
print("3. Squares of even numbers:", even_squares)

# 4. Using two lists — find common elements (intersection)
intersection = [x for x in list1 if x in list2]
print("4. Intersection:", intersection)

# 5. Cartesian product — pair every element of list1 with every element of list2
cartesian_product = [(x, y) for x in list1 for y in list2]
print("5. Cartesian product:", cartesian_product)

# 6. Filtered Cartesian product — pairs where sum is even
even_sum_pairs = [(x, y) for x in list1 for y in list2 if (x + y) % 2 == 0]
print("6. Pairs with even sum:", even_sum_pairs)

# 7. Flatten a nested list (list of lists)
nested_list = [[1, 2], [3, 4], [5]]
flattened = [item for sublist in nested_list for item in sublist]
print("7. Flattened list:", flattened)

# 8. Conditional expression inside comprehension — mark even numbers as "Even", odd as "Odd"
labels = ["Even" if x % 2 == 0 else "Odd" for x in list1]
print("8. Labels (Even/Odd):", labels)

# 9. Nested list comprehension — create a multiplication table (1 to 5)
multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("9. Multiplication Table:")
for row in multiplication_table:
    print(row)

# 10. Complex filtering and transformation — squares of numbers in list1 that are prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_squares = [x**2 for x in list1 if is_prime(x)]
print("10. Squares of primes:", prime_squares)
