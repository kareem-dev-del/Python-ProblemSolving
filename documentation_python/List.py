#***************************************************
#القوائم (List)
# إنشاء قائمة
numbers = [10, 20, 30, 40]

# طول القائمة
print(len(numbers))  # 4

# الوصول لعنصر محدد (مثل النصوص)
print(numbers[0])    # 10
print(numbers[2])    # 30

# تغيير قيمة عنصر
numbers[1] = 25
print(numbers)       # [10, 25, 30, 40]

# إضافة عنصر في آخر القائمة
numbers.append(50)
print(numbers)       # [10, 25, 30, 40, 50]

# إزالة عنصر
numbers.remove(30)
print(numbers)       # [10, 25, 40, 50]

# slicing - أخذ جزء من القائمة
print(numbers[1:3])  # [25, 40]

# التكرار على القائمة
for n in numbers:
    print(n)

equations = ["2x-10=0", "3x+6=0", "x-5=0"]

for eq in equations:
    print("حل المعادلة:", eq)


 #*************************************************************************
 # القواميس (Dict)   
# إنشاء قاموس
student = {
    "name": "Karim",
    "age": 20,
    "grade": "A"
}

# الوصول لقيمة عن طريق المفتاح
print(student["name"])   # Karim
print(student["age"])    # 20

# تغيير قيمة
student["age"] = 21
print(student)           # {'name': 'Karim', 'age': 21, 'grade': 'A'}

# إضافة مفتاح جديد
student["major"] = "IT"
print(student)           # {'name': 'Karim', 'age': 21, 'grade': 'A', 'major': 'IT'}

# إزالة مفتاح
del student["grade"]
print(student)           # {'name': 'Karim', 'age': 21, 'major': 'IT'}

# التكرار على القاموس
for key, value in student.items():
    print(key, ":", value)


solutions = {
    "2x-10=0": 5,
    "3x+6=0": -2,
    "x-5=0": 5
}

# الوصول لقيمة معينة
print(solutions["3x+6=0"])  # -2

# التكرار على كل المعادلات وحلولها
for eq, sol in solutions.items():
    print(f"المعادلة {eq} حلها x = {sol}")
