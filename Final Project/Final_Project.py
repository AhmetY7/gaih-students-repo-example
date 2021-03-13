questions = {"1 - Halı saha maçlarında hangisi genellikle görülmez?":"A) Köşe vuruşu\nB) Taç atışı\nC) Serbest vuruş\nD) Penaltı",
             "2 - 'Kıpırdamayın, çekiyorum, çekiyorum, çektim' diyen kişi muhtemelen kimdir?":"A) Ressam\nB) Dişçi\nC) Niyetçi\nD) Fotoğrafçı",
             "3 - 'Akçaabat', 'İnegöl', 'Tire' gibi yerlerin hangi tür yiyeceği meşhurdur?":"A) Dondurma\nB) Köfte\nC) Helva\nD) Kebap",
             "4 - Hangisi Türkçedeki ünlü harfleri iki karşı gruba ayıran başlıklardan biri değildir?":"A) Kalın-İnce\nB) Düz-Yuvarlak\nC) Geniş-Dar\nD) Sert-Yumuşak",
             "5 - Otomobil yıkamaya verilirken yıkanması gereken yerler genellikle nasıl belirtilir?":"A) İç dış\nB) Ön arka\nC) Alt üst\nD) Cam çerçeve",
             "6 - 'Çatallı' ifadesi hangisinin kusurlu olanı için kullanılır?":"A) Ses\nB) Görüntü\nC) Koku\nD) Tat",
             "7 - Halk arasında kullanılan söze göre hangisi kara gün içindir?":"A) Ak akçe\nB) Kuru bakır\nC) Acı kahve\nD) Keskin sirek",
             "8 - Ilgaz Dağları'nda dolaştığını söyleyen biri hangi iki il sınırları içerisinde geziyor demektir?":"A) Sakarya-Bolu\nB) Sinop-Samsun\nC) Kastamonu-Çankırı\nD) Amasya-Giresun",
             "9 - Hangisinin adıyla anılan ve atkı, hırka gibi kıyafetlerde kullanılan bir tür örgü biçimi vardır?":"A) Beyrut\nB) Üsküp\nC) Sofya\nD) Selanik",
             "10 - İlkokulda, sınıfta konuşanların ve yaramazlık yapanların adını tahtaya yazan öğrenci genellikle kim olur?":"A) Temizlik kolu başkanı\nB) İlk yardım kolu başkanı\nC) Sınıf başkanı\nD) Kütüphane kolu başkanı"}

true_answers = ["B","D","B","D","A","A","A","C","D","C"]

i = 0
sum = 0
for question,option in questions.items():
    print(question)
    print(option)
    user_answer = input("Cevap: ")
    while (len(user_answer) != 1) or (user_answer.upper() != "A" and user_answer.upper() != "B" and user_answer.upper() != "C" and user_answer.upper() != "D"):
        user_answer = input("Geçerli şık giriniz. Cevap: ")
    if true_answers[i] == user_answer.upper():
        sum += 10
    i += 1

if sum <= 50:
    print("Başarısız. Puanınız", sum)
else:
    print("Başarılı. Puanınız:", sum)