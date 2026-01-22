# encode: بنحوّل كل كلمة لشكل طولها#الكلمة ونلزقهم كلهم في String واحد عشان نبعته بأمان.

# decode: بنقرأ الرقم قبل # عشان نعرف طول الكلمة، وبناخد العدد ده من الحروف بعده ونكرر لحد ما النص يخلص.

#Day=>Three=>https://neetcode.io/


from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded    

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            hash_index = s.find('#', i)
            if hash_index == -1:
                break
            length = int(s[i:hash_index])
            word = s[hash_index + 1: hash_index + 1 + length]
            result.append(word)
            i = hash_index + 1 + length
        return result

# اختبار الكود
if __name__ == "__main__":
    sol = Solution()  # إنشاء كائن من الكلاس
    
    # اختبار التشفير
    encoded_str = sol.encode(["kareem", "Ali"])
    print("Encoded:", encoded_str)  # Output: 7#kareem3#Ali
    
    # اختبار فك التشفير
    decoded_list = sol.decode(encoded_str)
    print("Decoded:", decoded_list)  # Output: ['kareem', 'Ali']