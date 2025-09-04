fayl=input("fayl nomi:")
if fayl.endswith(".pdf"):
    print("Fayl turi: pdf")
elif fayl.endswith(".dock"):
    print("Fayl turi: word")    
elif fayl.endswith(".txt"):
     print("Fayl turi: oddiy text") 
else:
    print("Boshqa fayl turi")       