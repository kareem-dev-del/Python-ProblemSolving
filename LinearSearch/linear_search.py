# /*
# 📘 البرنامج: Linear Search in Java
# 🔍 الفكرة:
#     - عندنا مصفوفة أرقام.
#     - المستخدم يدخل رقم.
#     - نمر على كل عنصر في المصفوفة:
#         • لو لقيناه → نطبع مكانه (index).
#         • لو مش لقيناه → نطبع "Not Found".
# 🎯 الهدف: فهم طريقة البحث الخطي خطوة بخطوة.
# */
class linear_search:
    def __init__(self,numbers):
        self.numbers=numbers

    def search(self,target) :
        i=0  
        for i in range(len(self.numbers)):
            if numbers[i] == target:
                print(f"{target} numbers Found in indez {i}")
                return
        print(f"Not Found target {target}")   


numbers =[1,2,8,6,3,4,7,15,48] 
searcher = linear_search(numbers)
target = int(input("Enter target:"))
searcher.search(target)