cv1 = {"Ad:":"Ahmet", "Soyad:":"Tosun", "Yaş:": 26, "Telefon:":"555-05-07", "Adres:":"İstanbul", "Meslek:":"Bilgisayar Mühendisi", "Öğrenim Durumu:":"Lisans"}
cv2 = {"Ad:":"Okan", "Soyad:":"Ok", "Yaş:": 28, "Telefon:":"555-74-12", "Adres:":"Eskişehir", "Meslek:":"Kontrol Mühendisi", "Öğrenim Durumu:":"Yüksek Lisans"}
cv3 = {"Ad:":"Berat", "Soyad:":"Beyaz", "Yaş:": 25, "Telefon:":"555-60-87", "Adres:":"Antalya", "Meslek:":"Bilgisayar Mühendisi", "Öğrenim Durumu:":"Lisans"}
cv4 = {"Ad:":"Enes", "Soyad:":"Sarı", "Yaş:": 29, "Telefon:":"555-50-33", "Adres:":"Konya", "Meslek:":"Bilgisayar Mühendisi", "Öğrenim Durumu:":"Lisans"}
cv5 = {"Ad:":"Berke", "Soyad:":"Çiçek", "Yaş:": 30, "Telefon:":"555-90-01", "Adres:":"Samsun", "Meslek:":"Bilgisayar Mühendisi", "Öğrenim Durumu:":"Lisans"}

print("Cv of First Person\n-------------------")
for key,values in cv1.items():
    print(key, values)

print("\nCv of Second Person\n-------------------")
for key,values in cv2.items():
    print(key, values)

print("\nCv of Third Person\n-------------------")
for key,values in cv3.items():
    print(key, values)

print("\nCv of Fourth Person\n-------------------")
for key,values in cv4.items():
    print(key, values)

print("\nCv of Fifth Person\n-------------------")
for key,values in cv5.items():
    print(key, values)
