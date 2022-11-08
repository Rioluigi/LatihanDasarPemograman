def Luas_Segitiga():
    print("✨Hitung Luas Segitiga✨")
    alas = int(input('Masukan alasnya: '))
    tinggi = int(input('Masukan tingginya: '))
    Luas = 1/2 * (alas * tinggi)
    print("Luas Segitiga Adalah: ", Luas, ("cm2"))

def Luas_Persegi_Panjang():
    print('💥Hitung Luas Persegi Panjang💥')
    panjang = float(input('Masukan tingginya: '))
    lebar = float(input('Masukan lebarnya: '))
    Luas = (panjang * lebar)
    print("Luas Persegi Panjang Adalah: ", Luas, ("cm2"))

def Bilangan_Ganjil_Genap():
    print('🍳Menentukan Bilangan Ganjil dan Genap🍳')
    awal = int(input('Masukan Nilai Awal: '))
    akhir = int(input('Masukan Nilai Akhir: '))
    Ganjil = []
    Genap = []
    for i in range(awal, akhir+1):
        if i % 2 == 0:
            Ganjil.append(i)
        if i % 2 == 1:
            Genap.append(i)
    print('Bilangan Ganjil: ', Ganjil,)
    print('Bilangan Genap: ', Genap,)

while True:
    userInput = int(input(
        "MENU : \n1. Luas Segitiga\n2. Luas Persegi Panjang\n3. Menentukan Angka Ganjil Genap\n4. Quit\nPilih Nomer: "))
    if (userInput == 1):
        Luas_Segitiga()
    elif (userInput == 2):
        Luas_Persegi_Panjang()
    elif (userInput == 3):
        Bilangan_Ganjil_Genap()
    else:
        break