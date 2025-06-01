def string_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return string_palindrome(s, left + 1, right -1)

s = input("Enter a string: ").lower()
if string_palindrome(s, 0, len(s) - 1):
    print("Palindrome")
else: 
    print("Not Palindrome")