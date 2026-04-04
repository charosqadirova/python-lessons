text = "python lessons"
print(len(text)) # 14
# string ichidagi har bir belgi indexsga ega, (0 dan boshlanadi)
print(text[0]) # p
print(text[1]) # y
print(text[2]) # t
print(text[3]) # h
print(text[4]) # o
print(text[5]) # n
print(text[1]) 
print(text[len(text) -1 ])
# for loop
for belgi in text:
    print(belgi)
# 2-usul
for index in range(len(text)):
    print( index, text[index])
  