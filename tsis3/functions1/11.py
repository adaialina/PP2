word = input()
def palindrome(word):
    if word == word[::-1]:
        print('Yes')
        
    else:
        print('No')
        

palindrome(word)