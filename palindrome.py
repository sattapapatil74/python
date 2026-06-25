def is_palindrome(x):
    s=str(x)
    if s==s[:: -1]:
        return"palindrome"
    return"not palindrome"
print("123")