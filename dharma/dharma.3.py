# NAMA : MOCHAMMAD DHAARMA RAZHA S.
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
# tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi
# melebihi 20.000 dollar.
# Rumus: Nilai investasi tahun ke-n = Nilai investasi tahun ke-(n-1) + 6% dari Nilai investasi tahun ke-
# (n-1)
nilai_investasi = 10000  # Nilai investasi awal dalam dollar
target_nilai_investasi = 20000  # Nilai investasi yang diinginkan dalam dollar
tingkat_pertumbuhan = 0.06  # Tingkat pertumbuhan tahunan (6%)
tahun = 0  # Inisialisasi jumlah tahun
while nilai_investasi < target_nilai_investasi:
    nilai_investasi += nilai_investasi * tingkat_pertumbuhan  # Meningkatkan nilai investasi setiap tahun
    tahun += 1

print("Dibutuhkan", tahun, "tahun agar nilai investasi melebihi", target_nilai_investasi, "dollar.")