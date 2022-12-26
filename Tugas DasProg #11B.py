def Bayar_Kos(biaya_kos, keterlambatan, denda_terlambat):
  total_harga = biaya_kos + (keterlambatan * denda_terlambat)
  return total_harga
print("====================Total Harga======================")
total_harga = Bayar_Kos(850000, 5, 50000)
print('Total Harga Bayar Kos= ',round (total_harga))  
print("====================Total Harga======================")