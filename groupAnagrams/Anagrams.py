# البرنامج يجمع كلمات Anagrams مع بعضها في مجموعات حسب ترتيب الحروف
# الدالة groupAnagrams تستقبل أي عدد من الكلمات كـ arguments باستخدام *args

def groupAnagrams(*words):
    print("all words", words)
    if len(words) < 2:
        return [[]]  

    anagrams = {}
    
    for word in words:
        key = ''.join(sorted(word))      
        if key not in anagrams:          
            anagrams[key] = []
        anagrams[key].append(word)       

    return list(anagrams.values())       