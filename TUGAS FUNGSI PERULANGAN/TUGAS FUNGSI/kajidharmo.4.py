# NAMA : MOCHAMMAD DHARMA R S
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.
# Rumus: Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n
def hitung_jumlah_digit(bilangan):
    bilangan = abs(bilangan)  # Mengambil nilai mutlak dari bilangan (untuk menghindari bilangan negatif)
    jumlah_digit = 0
    while bilangan > 0:
        digit = bilangan % 10  # Mengambil digit terakhir
        jumlah_digit += digit  # Menambahkannya ke total jumlah digit
        bilangan //= 10  # Menghapus digit terakhir
    return jumlah_digit
# Contoh penggunaan fungsi hitung_jumlah_digit
bilangan = int(input("Masukkan bilangan: "))
hasil = hitung_jumlah_digit(bilangan)
print(f"Jumlah digit dari {bilangan} adalah {hasil}")
