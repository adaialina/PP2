text = input()
def s_reverse(text): 
    return ' '.join(text.split()[::-1])

result = s_reverse(text)
print(result)