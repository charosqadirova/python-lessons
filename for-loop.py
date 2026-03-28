# nums = [76, 12, 51, 50, 98]
# k = 0
# counter = 1
# for num in nums:
#     if num % 2 == 1:
#         k += num
#         counter += 1 
# print(k / counter)

# M = int(input("M sonini kiriting "))
# sonlar = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34, 92]
# k = 0
# for n in sonlar:
#     if M < n:
#         k += n ** 2
# print(k)

#122

# number = [33, -21, 14, -18, 76, 48, -26, 39, 72, 21, 0, -72]
# k = 0
# b = 0
# for num in number:
#     k += num ** 2
# s = len(number)
# b += num 
# c = b / s
# print(k)
# print(c)

#126
# import math
# sonlar = [7, 24, -5, 23, 99, -3, 24, 51]
# s = 0
# for son in sonlar:
#     s += son
# value = s / len(sonlar)
# avarage = math.log(value)
# print(avarage)

# for index in range(len(sonlar)):
#     if sonlar[index] < 0:
# print(sonlar)

#104

# m = [74, 0, 1, 33]
# l = min(m)
# k = m.index(m)
# m[k], m[-1], = m[-1], m[k]
# print(*m)

#127 
# numbers = [46, 23, -52, 34, 6, -18, 52]
# min_value = min(numbers)
# for index in range(len(numbers))
#    element = numbers[index]
#    if element < 0:
#     numbers[index] = min_value ** 2
#     print(numbers)

#110

# sonlar = [7, 11, 83, 18, 31, 31, 3]
# M = int(input("M sonnini kiriting"))
# K = int(input("K sonini kiriting"))
# m = 1
# for son in sonlar:
#     if son == K or son == M:
#         m *= son
# print(m)

#104  2-usul

# sonlar = [ 74, 0, 1, 33]
# min_value = min(sonlar)
# last_element = sonlar[-1]
# min_index = sonlar.index(min_value)

# sonlar[min_index] = last_element
# sonlar[-1] = min_value
# print(sonlar)

#124
# K = input("K sonini kiriting")
# numbers = [95,72,-47]
# max_value = max(numbers)
# index = numbers[k-1]
# max_value = index
# print(max_value)


# numbers = [29, 50, -14, 4, 27, -56]
# K = int(input("K sonini kiriting  "))
# max_value = max(numbers)
# max_index = numbers.index(max_value)
# numbers[max_index] = numbers[k - 1]
#  numbers[k - 1] = max_value
#  print(numbers)
# amaliyot
# a = 5
# b = 3
# #1- usul  temporary varible -- vaqtinchalik o'zgaruvchi
# c = a
a = b
b = c
print(a, b)
# 2- usul
a,b = b ,a
print(a, b)
#3- usul

















































































































