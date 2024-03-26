# Meminta pengguna untuk memasukkan jumlah nilai yang akan dihitung rata-ratanya
jumlah_nilai = int(input("Masukkan jumlah nilai: "))

# Inisialisasi variabel untuk menyimpan total nilai
total_nilai = 0

# Meminta pengguna untuk memasukkan nilai sebanyak yang diminta
for i in range(jumlah_nilai):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    total_nilai += nilai

# Menghitung nilai rata-rata
rata_rata = total_nilai / jumlah_nilai

# Mencetak nilai rata-rata
print(f"Nilai rata-rata dari {jumlah_nilai} nilai adalah: {rata_rata}")
