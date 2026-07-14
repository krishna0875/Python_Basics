def reverse_string(s: str) -> str:
        return s[::-1]

print(reverse_string("coach"))

def is_palindrome(s: str) -> bool:
        return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))

def factorial(n: int) -> int:
      if n == 0:
        return 1
      return n * factorial(n-1)

print(factorial(5))
