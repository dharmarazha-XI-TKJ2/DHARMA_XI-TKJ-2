# NAMA : MOCHAMMAD DHAARMA RAZHA S.
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan
# dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang
# menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.
# Rumus: Jumlah pembelahan setelah t menit = t / 20
waktu_total = 120  # Rentang waktu dalam menit
interval_pembelahan = 20  # Interval pembelahan dalam menit
jumlah_pembelahan = waktu_total // interval_pembelahan
print("Pembelahan bakteri terjadi sebanyak", jumlah_pembelahan, "kali dalam rentang waktu 2 jam.")