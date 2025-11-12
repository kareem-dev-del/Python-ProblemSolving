# /*
#  * البرنامج: حساب العامل (Factorial) باستخدام الاستدعاء الذاتي (Recursion)
#  * الوصف: يقوم هذا البرنامج بحساب العامل (Factorial) لعدد يُدخله المستخدم 
#  *       عن طريق دالة تستدعي نفسها Recursively.
#  * اللغة: Python
#  * الكاتب: كريم
#  */



def FactorialRecursions(number):
    if number < 1 :
        return 1
    else :
        return number * FactorialRecursions(number - 1)
num = int(input("Enter the number:"))
print(f"Factorial {num} is {FactorialRecursions(num)}")