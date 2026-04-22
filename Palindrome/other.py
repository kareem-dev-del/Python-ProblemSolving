
def Palindrome(word):
   
    clean_input = ""

    for c in word:
        if c.isalnum():
            clean_input += c.lower()
    print(clean_input) 
    start = 0
    end = len(clean_input) - 1 
    while( start < end ):
        if clean_input[start] != clean_input[end]: 
            return False
        start+=1
        end -=1
    return True 

#x="Was it a car or a cat I saw?"
x="L?evel  .  kareem@"
print(Palindrome(x))    