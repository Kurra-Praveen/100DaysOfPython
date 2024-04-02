import math
import string

x = "7 59 55 2354"
y = x.split()
print(max(y))

#
# def caesarCipher(s, k):n
#     sen = ""
#     small = string.ascii_lowercase
#     cap = string.ascii_uppercase
#     for each_char in s:
#
#         if each_char.isupper():
#             sen += cap[(cap.index(each_char) + k) % 26]
#         elif each_char.islower():
#             sen += small[(small.index(each_char) + k) % 26]
#
#         else:
#             sen += each_char
#
#     return sen
#
#
# alp = string.ascii_lowercase
# x = (alp.index("a") + 87) % 26
# print(x, alp[x])
# f = caesarCipher("www.abc.xy", 87)
# print(f)
