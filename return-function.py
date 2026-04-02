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