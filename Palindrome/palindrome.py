# /*
#  * البرنامج: التحقق من الـ Palindrome
#  * الوصف: يقوم هذا البرنامج بقراءة كلمة أو جملة من المستخدم،
#  *       ثم يتحقق إذا كانت الكلمة أو الجملة تقرأ نفسها من الأمام إلى الخلف (Palindrome) أم لا.
#  *       البرنامج يتجاهل المسافات والحروف الكبيرة أثناء المقارنة.
#  * اللغة: python
#  * الكاتب: كريم
#  */
def Palindrome(word):
    letters = list(word)
    start =0
    end = len(letters)-1
    isPalindrome =True
    while(start < end):
        if letters[start] != letters[end] :
            isPalindrome = False
            break
        start+=1
        end-=1
    return isPalindrome
word =input("Enter Palindrome word:") 
clean_input = word.replace(" ", "").lower()
if Palindrome(clean_input):
    print("The word is a Palindrome")   
else :
   print("The word is  not a Palindrome")   



