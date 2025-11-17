# */
#  * البرنامج: ترتيب الأعداد باستخدام خوارزمية الفقاعات (Bubble Sort)
#  * الوصف: يقوم هذا البرنامج بترتيب مصفوفة من الأعداد تصاعديًا 
#  *       عن طريق مقارنة كل عنصر بالعنصر الذي يليه وتبديلهما إذا كان الترتيب غير صحيح.
#  * اللغة: Python
#  * الكاتب: كريم
# ### /*
def BubbleSort(arra):
   
    for i in range(len(arra)):
        for j in range(len(arra) - i - 1):
            if arra[j] > arra[j+1]:
               arra[j],arra[j+1] = arra[j+1],arra[j]
               
    return arra             
    
array =[1,7,3,4,9,2,8,1,0] 
print(BubbleSort(array)) 