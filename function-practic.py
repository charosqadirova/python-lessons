  # 1
name = input("Ismingizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))
tugilgan_yil = 2026 - age
yosh_hisobla(name, tugilgan_yil)
 # 2
 def kvadrat_kub(son):
     kvadrat = son ** 2
     kub = son ** 3
      print(f"{son} sonining kvadrati {kvadrat} ga, kubi esa {kub} ga teng")

son = int(input("Son kiriting: "))
kvadrat_kub(son)
 # 3
 def juft_toq(n):
    if n % 2 == 0:
        print("Juft")
    else:
        print("Toq")

# Foydalanuvchidan son olish
son = int(input())
juft_toq(son)
# 4
def katta_kichik(a, b):
    if a > b:
        print(f"{a} katta, {b} kichik")
    elif a < b:
        print(f"{b} katta, {a} kichik")
    else:
        print("Sonlar teng")

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
katta_kichik(a, b)
# 5
def daraja(x,y):
    
    print(f"{x} ning {y} darajasi {natija} ga teng")
x = int(input("Son kiriting: "))
y = int(input("Daraja kiriting: "))

daraja(x, y)

                                                                                                                                        

    