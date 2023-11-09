# NAMA : MOCHAMMAD DHAARMA RAZHA S.
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
# jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa
# apel kurang dari 20 buah.
# Rumus: Sisa apel hari ke-n = Sisa apel hari ke-(n-1) - 10% dari Sisa apel hari ke-(n-1)
jumlah_apel = 100  # Jumlah apel awal
sisa_apel_terakhir = jumlah_apel  # Inisialisasi jumlah apel terakhir
target_sisa_apel = 20  # Jumlah sisa apel yang diinginkan
hari = 0  # Inisialisasi jumlah hari
while sisa_apel_terakhir > target_sisa_apel:
    jumlah_terjual = sisa_apel_terakhir * 0.10  # Jumlah yang dijual setiap hari (10% dari sisa apel)
    sisa_apel_terakhir -= jumlah_terjual  # Mengurangi sisa apel setiap hari
    hari += 1

print("Dibutuhkan", hari, "hari agar sisa apel kurang dari", target_sisa_apel, "buah.")
