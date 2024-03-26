def cek_kelulusan(nilai):
    if nilai >= 65:
        return "LULUS"
    else:
        return "TIDAK LULUS"

def main():
    try:
        nilai = float(input("Masukkan nilai mahasiswa: "))
        if nilai < 0 or nilai > 100:
            print("Nilai harus dalam rentang 0 hingga 100.")
        else:
            status = cek_kelulusan(nilai)
            print(f"Mahasiswa dinyatakan {status}.")
    except ValueError:
        print("Masukkan harus berupa angka.")

if __name__ == "__main__":
    main()
