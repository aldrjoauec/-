x=int(input())

def isPalindrome():
    x = str(x)
    x_1 = x
    x_1 = str(x_1)
    x_1 = x_1[::-1]
    if x == x_1:
        return True
    else:
        return False
print(d=isPalindrome())