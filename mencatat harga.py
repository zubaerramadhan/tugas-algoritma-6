harga_list = []

while True:
    harga_input = input("Masukkan harga (ketik 'stop' untuk berhenti): ")
    
    if harga_input.lower() == 'stop':
        break
    
    try:
        harga = int(harga_input)
        harga_list.append(harga)
    except ValueError:
        print("Input tidak valid. Masukkan harga atau 'stop'.")

if harga_list:
    harga_tertinggi = max(harga_list)
    harga_terendah = min(harga_list)
    
    print(f"Harga tertinggi: {harga_tertinggi}")
    print(f"Harga terendah: {harga_terendah}")
else:
    print("Tidak ada harga yang dimasukkan.")