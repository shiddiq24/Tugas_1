teori = int(input("masukkan nilai teori:"))
praktek = int(input("masukkan nilai praktek:"))
if (teori>=70) & (praktek>=70):
   print("Selamat, anda lulus!")
elif (praktek<=70) & (teori>=70):
  print("anda harus mengulangi ujian praktek!")
elif (teori<=70) & (praktek>=70):
  print("anda harus mengulangi ujian teori!")
else:
  print("anda harus mengulangi ujian praktek dan teori!")   