# NAMA : MOCHAMMAD DHAARMA RAZHA S.
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah
# ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung
# berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.
jumlah_ayam = 100  # Jumlah awal ayam
target_ayam = 200  # Jumlah ayam yang diinginkan

bulan = 0  # Inisialisasi jumlah bulan

while jumlah_ayam <= target_ayam:
    jumlah_ayam += jumlah_ayam * 0.05  # Menambahkan 5% ayam setiap bulan
    bulan += 1

print("Dibutuhkan", bulan, "bulan agar jumlah ayam melebihi", target_ayam, "ekor.")
