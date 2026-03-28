# string, int, float, bool, dictonary, list
data types (malumot turlari)
thisdict = {
"brand": "Fard",
"model": "Mustang",
"year":1964,
"color":"red",
"price": 45000
}
print(thisdict)
print(type(thisdict))


user = {
  "name": "Charos",
  "age": 14, 
  "is_student": True,
  "hobbies": ["reading", "coding", "gaming"],
  "email" : "charosqadirova13@gmail.com"
}

# key-value pair (kalit-qiymat juftligi)
# 1. valularni olish (kalit orqali)
print(user['name'])
print(type(user))

for book in user['hobbies']:
    print(book)

# 2.Yangi key-value qo'shish
users["country"] = "Uzbekistan"
print(users)

# 3. Bo'sh lug'at (empy dictionary) yaratish
talaba_1 = {}
talaba_1["ism"] = "Qobuil Rasulov"
talaba_1["yosh"] = 20
print(talaba_1)
print(f"talaba {talaba_1['ism'].title()} {talaba_1['yosh']} yoshda " )

# 4. key-value juftligini o'chrish
talaba_0 = {'ism': 'Murod Olimov', 'yosh': 20}
del talaba_0['yosh']
print(talaba_0)

# 5. get() metodi
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }

print(telefonlar['ali'])
print(f"Alining telefoni {telefonlar['ali']}")


