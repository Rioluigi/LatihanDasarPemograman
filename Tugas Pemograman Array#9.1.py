import array as myarray
alfabet = []
stop = False
i = 1 
while (not stop):
    huruf_alfabet = input("ketikan huruf alfabet yang ke - {} :".format(i))
    alfabet.append(huruf_alfabet)
    i+=1 
    tanya=input("Mau isi data lagi atau tidak?(Y Or T): ")
    if(tanya=="t"):
        stop=True 
        print("=========================================")
        print("jadi,huruf vocal ada 9 dan huruf konsonan ada 1 : ",alfabet)
