# 1. القاعدة الأساسية
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# 2. مع شرط if
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4]

# 3. شرط if else
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# 4. Nested List Comprehension
table = [[i*j for j in range(1,4)] for i in range(1,4)]
print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 5. Flatten Nested List
nested = [[1,2], [3,4], [5,6]]
flat = [num for sublist in nested for num in sublist]
print(flat)  # [1, 2, 3, 4, 5, 6]

# 6. التعامل مع String
word = "hello"
chars = [c for c in word]
print(chars)  # ['h', 'e', 'l', 'l', 'o']

text = "Python is fun"
no_spaces = [c for c in text if c != ' ']
print(no_spaces)  # ['P','y','t','h','o','n','i','s','f','u','n']

# 7. استخدام Functions
def square(x):
    return x**2

squares2 = [square(n) for n in numbers]
print(squares2)  # [1, 4, 9, 16, 25]

# 8. Tuples و Dicts
tuples = [(n, n**2) for n in numbers]
print(tuples)  # [(1,1), (2,4), (3,9), (4,16), (5,25)]

squares_dict = {n: n**2 for n in numbers}
print(squares_dict)  # {1:1, 2:4, 3:9, 4:16, 5:25}
