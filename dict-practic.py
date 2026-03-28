

# 1- amaliyot
dad = {'ismi':'Sardor',
 'yil':1987,
 'viloyat':'Xorazm'}
yil = dad['yil']
viloyat = dad['viloyat']
print(f"Otamning ismi {dad['ismi'].title()}, {yil}-yilda, {viloyat.title()} viloyatida tug'ilgan")

# 2- amaliyot
taomlar = {
    'Imona':'lag'mon',
    'Shabnam':'osh',
    }

print(taomlar['Imona'])
print(f"Imonaning taomi {taomlar['Imona']}")

print(taomlar['Shabnam'])
print(f"Shabnamning taomi {taomlar['Shabnam']}")

# 3-amaliyot (get() metodi)
phone = {
    "brand":"Apple",
    "model": "iphone 13 pro max",
    "color":"silver",
    "storage":"256GB",
    "price": 15000
}
print(phone.get("brand"))
print(phone.get("model"))
print(phone.get("color"))
print(phone.get("storage"))
print(phone.get("price"))

# 4- amaliyot (items() metodi)
print(phone.items())
for key, value in phone.items():
    print(f"Kalit: {key},
    Qiymat: {value}")
     
# 5- amaliyot (keys() metodi)
print(phone.keys())
print(telefonlar.keys())
#  
mahsulotlar = { # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }

print(mahsulotlar.keys())  

print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 6- amaliyot 
# 1. List elementlari orasida qiymatining mavjudligini tekshirish
# 2. Kalitni ro'yxatda mavjudligini tekshirish
bozorlik = ['anor','uzum','non','baliq']
mahsulot = input("Nima xarid qilmoqchisiz? ")
if mahsulot in bozorlik:
    print(f"{mahsulot.title()} do'konimizda bor")
else:   
  print(f"{mahsulot.title()} do'konimizda yo'q")

# Amaliyotlar
# izohli lug'at
lugat = {
    'integer':'Butun son',
    'float':"O'nlik son",
    'string':'Matn',
    'boolean':'Mantiqiy qiymat'
    'if': "shartlarni tekshirish",
    'list': "Ro'yxat",
    'input': "Foydalanuvchi kiritgan ma'lumot",
    'tuple': "O'zgarmas ro'yxat",
    'dictionary': "Kalit-qiymat juftliklari to'plami",
    'print': "Natijani ekranga chiqarish"
}
for key, value in lugat.items():
    print(f"{key.title()}  {value}")
# 1
davlatlar = {
    'O\'zbekiston':'Toshkent',
    'Rossiya':'Moskva',
    'AQSH':'Vashington',
    'Xitoy':'Pekin',
    'qozog\'iston':'Nursulton',
    'indoneziya':'Jakarta',
    'turkiya':'Anqara',
    'italiya':'Rim',
    'fransiya':'Parij',
    'germaniya':'Berlin'
}

 for davlat, poytaxt in davlatlar.items():
    print(f"{davlat.title()}ning poytaxti {poytaxt.title()} shahri") 

    print("dunyodagi davlatlar va ularning poytaxtlari:")
    for davlat in davlatlar.keys():
        print(davlat.title())
    print("dunyodagi davlatlar va ularning poytaxtlari:")
    for poytaxt in davlatlar.values():
        print(poytaxt.title())

key = input("Davlat nomini kiriting: ")
if key in davlatlar:
    print(f"{key.title()}ning poytaxti {davlatlar[key].title()} shahri")
else:    print(f"{key.title()} haqida ma'lumot topilmadi")

