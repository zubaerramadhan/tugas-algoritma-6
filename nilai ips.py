def hitung_ips():
    print("=== Penghitung Indeks Prestasi Semester (IPS) ===")
    
    jumlah_mata_kuliah = int(input("Masukkan jumlah mata kuliah: "))
    
    total_bobot = 0
    total_sks = 0
    
    for i in range(1, jumlah_mata_kuliah + 1):
        print(f"\nMata Kuliah {i}:")
        nilai = input("Masukkan nilai (A, B, C, D): ").upper()
        sks = int(input("Masukkan jumlah SKS: "))
        
        if nilai == "A":
            bobot = 4
        elif nilai == "B":
            bobot = 3
        elif nilai == "C":
            bobot = 2
        elif nilai == "D":
            bobot = 1
        else:
            print("Nilai tidak valid, masukkan nilai A, B, C, atau D.")
            continue
        
        total_bobot += bobot * sks
        total_sks += sks
    
    if total_sks == 0:
        print("\nTotal SKS tidak boleh nol. Program dihentikan.")
    else:
        ips = total_bobot / total_sks
        print(f"\nIndeks Prestasi Semester (IPS): {ips:.2f}")

hitung_ips()