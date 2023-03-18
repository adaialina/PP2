import os

def exists(file):
    if os.path.exists(file):
        return True
    else:
        return False 
    
a = r'C:\Users\User\OneDrive\Документы\пп2\tsis6\dir-and-files\alina.txt'
print(exists(a))
print(a)