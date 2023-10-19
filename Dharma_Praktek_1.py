#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#destinasi waktu yang selesai
#Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon
#berdasarkan aturan berikut:
#Jika total belanjaan lebih dari 500.000, berikan diskon 10%.
#Jika total belanjaan antara 300.000 dan 500.000, berikan diskon 5%.
#Jika total belanjaan kurang dari 300.000, tidak ada diskon.

def hitung_diskon(total_belanjaan):
    if total_belanjaan > 500000:
        diskon = 0.10
    elif total_belanjaan >= 300000:
        diskon = 0.05
    else:
        diskon = 0.00
    
    return diskon

def main():
    total_belanjaan = float(input("Masukkan total belanjaan: "))

    diskon = hitung_diskon(total_belanjaan)
    jumlah_diskon = total_belanjaan * diskon
    total_bayar = total_belanjaan - jumlah_diskon

    print(f"Total belanjaan: Rp {total_belanjaan:.2f}")
    print(f"Diskon: {diskon * 100:.2f}%")
    print(f"Jumlah diskon: Rp {jumlah_diskon:.2f}")
    print(f"Total bayar: Rp {total_bayar:.2f}")

if __name__ == "__main__":
    main()






