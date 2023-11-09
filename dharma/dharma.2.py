# NAMA : MOCHAMMAD DHAARMA RAZHA S.
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai
# dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program
# yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10
# kilometer.
jarak_awal = 5  # Jarak awal dalam kilometer
target_jarak = 10  # Jarak yang diinginkan dalam kilometer
minggu = 0  # Inisialisasi jumlah minggu
while jarak_awal <= target_jarak:
    jarak_awal += jarak_awal * 0.10  # Meningkatkan jarak sebesar 10% setiap minggu
    minggu += 1

print("Dibutuhkan", minggu, "minggu agar pelari dapat berlari lebih dari", target_jarak, "kilometer.")

