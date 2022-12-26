#No 1
def Luas_Segitiga():
    print('=========================')
    print("✨Hitung Luas Segitiga✨")
    print('=========================')
    alas = int(input('Masukan alasnya : '))
    tinggi = int(input('Masukan tingginya : '))
    Luas = 1/2 * (alas * tinggi)
    print("Luas Segitiga = ", round (Luas))

def Luas_Persegi_Panjang():
    print('================================')
    print('💥Hitung Luas Persegi Panjang💥')
    print('================================')
    panjang = float(input('Masukan tingginya : '))
    lebar = float(input('Masukan lebarnya : '))
    Luas = (panjang * lebar)
    print("Luas Persegi Panjang = ", round (Luas))

def Keliling_Persegi_Panjang():
    print("========================")
    print("keliling Persegi panjang")
    print("========================")
    p = float(input("Masukan Panjang : "))
    l = float(input("Masukan Luas : "))
    keliling = 2*(p + l)
    print('Keliling Persegi Panjang = ', round (keliling))

def Keliling_Lingkaran():
    print("=======================")
    print("💢Keliling Lingkaran💢")
    print("=======================")
    d = float(input("Masukkan Diameter : "))
    keliling = 3.14 * d
    print('Hasil Dari Keliling = ', round (keliling,2))

while True:
    userInput = int(input(
        "🍳MENU RUMUS BY RIO🍳 : \n1. Luas Segitiga\n2. Luas Persegi Panjang\n3. Keliling Persegi Panjang\n4. Keliling Lingkaran\n5. Selesai\nPilih Nomer: "))
    if (userInput == 1):
        Luas_Segitiga()
    elif (userInput == 2):
        Luas_Persegi_Panjang()
    elif (userInput == 3):
        Keliling_Persegi_Panjang()
    elif (userInput == 4):
        Keliling_Lingkaran()
    else:
        break
