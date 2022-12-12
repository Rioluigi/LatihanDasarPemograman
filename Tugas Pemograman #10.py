#List, Tuple and Dictionary By Rio
print("========================ini List======================")
#Nilai list maximal
a = [456,700,200,1000,2000]
print("Nilai dari List :",(a))
print ("Hasil dari maximal nilai list:",max(a))
print("="*54)

#Nilai list minimal
a = [456,700,200,1000,2000]
print("Nilai dari List :",(a))
print ("Hasil dari minimal list:",min(a))
print("="*54)

#Memasukan nilai pada list
a = ['a','e','i','u']
print("Original list :",a)
("/n")
a [2] =['o','a','e','i','u']
print("Memasukan Huruf pada list :",a[2])

("/n")
print("=======================ini Tuple======================") 
#Tuple ke format string
a = "g", "a", "n", "t","e","n","g"
print("Tuple Original :",(a))
print('ganteng')
print('='*54)

#Nilai Tuple Maximal
a = ("0","200","1000","2","9000","3","10")
print('Nilai Tuple :',(a))
print('Nilai Maximal :',max(a))
print('='*54)

#Nilai Tuple Minimal
a = ("2","200","1000","0","9000","3","10")
print('Nilai Tuple :',(a))
print('Nilai Minimal :',min(a))
print('='*54)

('/n')
print("======================Dictionary======================")
nilai ={
        1: 400,
        2: 800,
        3: 200,
        4: 6000,
        5: 100,
}
nilai_minimum = min(nilai.values())
print('Nilai minimun Dict :',(nilai_minimum))
print('='*54)

