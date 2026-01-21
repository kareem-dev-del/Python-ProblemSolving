# نعد كل عنصر في القائمة ونخزن التكرارات في قاموس count
# نحول القاموس لقائمة items عشان نقدر نختار أعلى k تكرارات بسهولة
# نكرر k مرات: كل مرة نختار العنصر الأكثر تكرارًا، نضيفه للنتيجة، ونشيله من القائمة



def x(nums):
   count= {}
   items= []
   result = []

   
   for num in nums:
        if num in count:
            count[num] += 1
        else:
           count[num] = 1  


   for key in count:
       items.append([key,count[key]])


   for _ in range(1):
       max_freq=-1
       max_item=None
       for item in items:
           if item[1] > max_freq:
               max_freq=item[1]
               max_item=item
          
       result.append(max_item)
       items.remove(max_item) 
   return result  

    
print(x([1,2,3,2,4,5,1]) ) 