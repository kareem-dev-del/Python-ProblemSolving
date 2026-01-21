# البرنامج يجمع كلمات Anagrams مع بعضها في مجموعات حسب ترتيب الحروف
# الدالة groupAnagrams تستقبل أي عدد من الكلمات كـ arguments باستخدام *args
#Day => One


# dict: لازم تتحقق من المفتاح قبل الإضافة

# defaultdict: المفتاح يتخلق تلقائيًا مع القيمة الافتراضية



from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))  # ترتيب الحروف
    anagrams[key].append(word)

print(anagrams)

#other solve==================================
# anagrams={}
# for word in words:
#     key = ''.join(sorted(word))  # ترتيب الحروف
#     if  key  not in anagrams:
#       anagrams[key]= []
#     anagrams[key].append(word)

# print(anagrams)
