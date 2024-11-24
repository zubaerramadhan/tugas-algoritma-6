print("Selamat datang di Kalkulator Deret Pintar!\n\n")

jumlahBilangan = int(input("Masukkan Banyaknya bilangan, kemudian ENTER: \n"))

totalBilangan = 0
rerataBilangan = 0

print("Deret bilangan: ", end='')

i = 1
while i <= jumlahBilangan:
    if i == jumlahBilangan: 
        print(i, end="")
    else:
        print(i, end=" + ")
    
    totalBilangan += i 
    i += 1 
print(f"\nTotal seluruh bilangan jika dijumlahkan: {totalBilangan}")
rerataBilangan = totalBilangan / jumlahBilangan

print(f"Rata-ratanya adalah {rerataBilangan}")