# /*
#  * البرنامج: التحقق من الـ Palindrome
#  * الوصف: يقوم هذا البرنامج بقراءة كلمة أو جملة من المستخدم،
#  *       ثم يتحقق إذا كانت الكلمة أو الجملة تقرأ نفسها من الأمام إلى الخلف (Palindrome) أم لا.
#  *       البرنامج يتجاهل المسافات والحروف الكبيرة أثناء المقارنة.
#  * اللغة: python
#  * الكاتب: كريم
#  */ 
def Palindrome(s):
     cleaned =''.join(char.lower() for char in s if char.isalnum())

     return cleaned == cleaned[::-1]
print(Palindrome("leviel"))


   
 


