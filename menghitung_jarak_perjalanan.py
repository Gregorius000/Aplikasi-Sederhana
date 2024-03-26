def hitung_jarak_perjalanan(kecepatan, waktu):
    jarak = kecepatan * waktu
    return jarak

def main():
    try:
        kecepatan = float(input("Masukkann kecepatan perjalanan anda (kam/jam): "))
        waktu = float(input("Masukkan waktu perjalanan anda (jam): "))

        jarak = hitung_jarak_perjalanan, waktu

        print(f"Jarak perjalanan adalah {jarak} kilometer.")
    except ValueError:
        print("Masukkan harus berupa angka.")

if __name__== "__main__":
    main()