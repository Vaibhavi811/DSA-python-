# Reverse a string using recursion
def rev_string(str,len):
    if len==0:
        return ""
    else:
        return str[len-1] + rev_string(str, len-1)
    
print(rev_string("Ishu",4))
        
    