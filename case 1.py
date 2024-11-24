jmlPisangGoreng = int(input("Banyak pisang goreng yang ingin dihitung: \n"))
hargaSatuan = int(input("Harga per biji: \n"))

print("Daftar harga pisang goreng:")

i = 1
while i <= jmlPisangGoreng:
    totalHarga = i * hargaSatuan
    print(f"{i}. Pisang goreng: \t Rp {totalHarga}")
    i += 1