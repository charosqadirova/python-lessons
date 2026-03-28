# function - ma' lum bir vazifzni bajaradigan kod bloklari
# ularni qayta ishlatish mumlin va ular dastur tuzilishini yaxshilaydi
# parametrlar - funksiya ichida ishlatiladigan o'zgaruvchilar
# argumentlar - funksiya chaqirilganda beriladigan qiymatlar
# 1
def salom_ber(ism):
    print(f"Salom, {ism}!")

salom_ber("Ali") 
salom_ber("Vali")

def yigindi(a, b):
 print(a + b)

yigindi(5, 10)
yigindi(3, 7)

# print(), list(), range(), len(), str(), int(), float() kabi funksiyalar Pythonning o'rnatilgan funksiyalaridir
# call - funksiya chaqirish
# def - funksiya ta'riflash
# declaration - funksiya e'lon qilish

def yosh_hisobla(ism, tugilgan_yil):
  yosh = 2026 - tugilgan_yil
    print(f"{ism}ning yoshi: {yosh}")

yosh_hisobla("Ali", 1990) # Alining yoshi: 36   
yosh_hisobla("Vali", 1985) # Valining yoshi: 41

