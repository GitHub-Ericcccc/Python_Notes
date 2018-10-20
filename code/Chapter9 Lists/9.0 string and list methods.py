# Some questions about string, list and their methods.
# str.method() returns a copy of str.
# lst.method() changes the lst and returns None.

str = '          adfsdfsdf'
print(str)

str.strip()
print(str)
print(str.strip())

nstr = str.strip()
print(nstr)


lst = ['d','e','a','c']
print(lst)

lst.sort()
print(lst)
# 输出排序后列表

print(lst.sort())
# 输出none

nlst = lst.sort()
print(nlst)
# 输出none

nlst = sorted(lst)
print(nlst)
# 输出排序后列表

print(lst.sort()==sorted(lst))
print(lst.sort()!=sorted(lst))
# 输出False 因为 None != sorted list.