string = "geeks for geeks121"

def isVowel(ch):
    return ch.upper() in ['A' ,'E' , 'I' ,'O' , 'U']


def countVowels(str , n):
    if (n == 1):
        return isVowel(str[n-1])
    
    return (countVowels(str , n-1)) + isVowel(str[n-1])

# string object 
str = "abc de"; 
print(isVowel('a'))

print(True + True)
  
# Total numbers of Vowel 
print(countVowels(str, len(str))) 
  