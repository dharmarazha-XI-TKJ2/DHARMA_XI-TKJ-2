#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#Buat program Python yang mengambil nilai performa karyawan (1 hingga 5, dengan 5 sebagai
#performa terbaik) dan menghitung bonus tahunan berdasarkan aturan berikut:
#• Performa 5: Bonus 20% dari gaji tahunan.
#• Performa 4: Bonus 10% dari gaji tahunan.
#• Performa 3: Bonus 5% dari gaji tahunan.
#• Performa 2: Bonus 2% dari gaji tahunan.
#• Performa 1: Tidak ada bonus.

def hitung_bonus(performa, gaji_tahunan):
    if performa == 5:
        bonus = 0.20 * gaji_tahunan
    elif performa == 4:
        bonus = 0.10 * gaji_tahunan
    elif performa == 3:
        bonus = 0.05 * gaji_tahunan
    elif performa == 2:
        bonus = 0.02 * gaji_tahunan
    else:
        bonus = 0.00
    
    return bonus

def main():
    performa = int(input("Masukkan nilai performa karyawan (1-5): "))
    gaji_tahunan = float(input("Masukkan gaji tahunan karyawan: "))

    if performa < 1 or performa > 5:
        print("Nilai performa tidak valid. Harap masukkan nilai antara 1 hingga 5.")
        return

    bonus = hitung_bonus(performa, gaji_tahunan)
    
    print(f"Bonus tahunan: Rp {bonus:.2f}")

if __name__ == "__main__":
    main()






