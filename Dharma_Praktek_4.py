#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#Buat program Python yang mengambil total belanjaan dan status anggota
#Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak,
#berikan diskon 10%.
#Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan
#diskon 0%.

#meminta input total belanjaan dan status anggota
total_belanjaan = float(input("masukkan total belanjaan "))
status_anggota = input("masukkan status anggota (premium/biasa): ")

# Inisialisasi varibel diskon
def hitung_diskon(total_belanja, status_anggota):
    if status_anggota == "premium":
        if total_belanja > 500000:
            diskon = 0.15
        else:
            diskon = 0.10
    else:
        if total_belanja > 300000:
            diskon = 0.07
        else:
            diskon = 0.00

    return diskon

def main():
    total_belanja = float(input("Masukkan total belanjaan: "))
    status_anggota = input("Apakah Anda anggota premium atau biasa? ").lower()

    if status_anggota not in ["premium", "biasa"]:
        print("Status anggota tidak valid. Harap masukkan 'premium' atau 'biasa'.")
        return

    diskon = hitung_diskon(total_belanja, status_anggota)
    jumlah_diskon = total_belanja * diskon
    total_bayar = total_belanja - jumlah_diskon

    print(f"Total belanjaan: Rp {total_belanja:.2f}")
    print(f"Diskon: {diskon * 100:.2f}%")
    print(f"Jumlah diskon: Rp {jumlah_diskon:.2f}")
    print(f"Total bayar: Rp {total_bayar:.2f}")

if __name__ == "__main":
    main()









