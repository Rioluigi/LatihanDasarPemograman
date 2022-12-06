import array as myarry
lulus = ['A','B+','B','C+','C']
tidak_lulus = ['D','E','F']

list_nilai =[9]
jumlah_mahasiswa = int(input("Masukan Jumlah Data mahasiswa : "))
Nim_mahasiswa = int(input("Masukan Nim Mahasiswa :"))
Masukan_nilai_UTS = int(input("Masukan nilai UTS :"))
Masukan_nilai_UAS = int(input("Masukan nilai UAS :"))
print('=' * 85)
# print("1Nim Nilai UTS pnilai UAS Total  Grade  Keterangan")
print("Nim           |      Nilai UTS    |  Nilai UAS    |     Total | Grade | Keterangan")
print('=' * 85)

nilai = (Masukan_nilai_UTS + Masukan_nilai_UAS ) / 2
if nilai >= 90:
    Grade = 'A'

elif nilai >= 80:
    Grade = 'B+'

elif nilai >= 70:
    Grade = 'B'
        
elif nilai >= 60:
    Grade = 'C+'

elif nilai >= 50:
    Grade = 'C'

elif nilai >= 40:
    Grade = 'D'
        
elif nilai >= 30:
    Grade = 'E'
    
else:
    Grade = 'F'
    

if Grade in lulus:
    print(Nim_mahasiswa,end='\t\t')
    print(Masukan_nilai_UTS,end='\t\t')
    print(Masukan_nilai_UAS,end='\t\t')
    print(nilai,end='\t')
    print(Grade,end='\t')
    print('LULUS',end='\t')
    

else:
    print(Nim_mahasiswa,end='\t\t')
    print(Masukan_nilai_UTS,end='\t\t')
    print(Masukan_nilai_UAS,end='\t\t')
    print(nilai,end='\t')
    print(Grade,end='\t')
    print('TIDAK LULUS',end='\n')
    print('=' * 85)