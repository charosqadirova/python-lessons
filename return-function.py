def add_numbers(a,b):
   print(a + b)
add_numbers(5, 10) # 15
add_numbers(3, 7) # 10

def add_numbers(c, d):
   return c + d
# qiymat qaytaruvchi qiymat - return
   print(add_numbers(5, 10)) # 15
   result = add_numbers(3, 7)
   print(result) # 10

# 1
a = int(input("son kiriting: "))
if  a / 2 :
    print("juft")
else:
   print("toq") 

 # 2  
   
def isEven(number):
    if number % 2 == 0:
        return "juft"
    else:
        return "toq"
print(isEven(4)) # juft
print(isEven(7)) # toq

# 3
def isEven(number):
    return "juft" if number % 2 == 0 else "toq"
print(isEven(12)) # juft
print(isEven(23)) # toq


# 4
# unli harflar = ['a', 'i', 'u', 'e', 'o']
# masalan: "salom" => 2 ta unli (a, o)
vowles = ['a', 'i', 'u', 'e', 'o']
def count_vowels(word):
    count = 0 
    for letter in word.lower():
        if letter in vowles:
            count += 1
    return count
print(count_vowels("salom")) # 2

