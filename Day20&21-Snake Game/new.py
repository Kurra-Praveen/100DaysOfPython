# a = [1, 2, 3, 4, 5,6,7]
# k=int((len(a)+1)/2)
# x=a[:k-1]
# y=a[k-1::][::-1]
# print(x+y)

# def timeConversion(s):
#     unit = s[::-1][:2][::-1]
#     if unit == "PM":
#         first_two = int(s[:2])
#         remaining = s[2:len(s) - 2]
#         convert = str(12 + first_two)
#         return convert + remaining
#     elif unit == "AM":
#         first_two = int(s[:2])
#         remaining = s[2:len(s) - 2]
#         if first_two == 12:
#             return "00" + remaining
#         else:
#             return s[:len(s) - 2]
#
#
# print(timeConversion("06:40:03AM"))

# def repeatedString(s, n):
#     if n <= len(s):
#         return s[:n].count('a')
#     if n > len(s):
#         count = s.count('a') * int(n / len(s)) + s[:n % len(s)].count('a')
#
#     return count,n/len(s),n%len(s)
# new_string = s
# if len(s) < n:
#     x = True
#     while x:
#         for each in s:
#             if len(new_string) >= n:
#                 x = False
#                 break
#             else:
#                 new_string += each
# else:
#     new_string = s[:n]
# b = new_string.count("a")
# return b, new_string


# print(repeatedString("abc", 10))
