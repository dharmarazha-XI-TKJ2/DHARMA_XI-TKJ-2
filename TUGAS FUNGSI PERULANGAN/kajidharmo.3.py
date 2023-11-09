# NAMA : MOCHAMMAD DHARMA R S
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
# dengan eksponen tertentu.
# Rumus: Bilangan^Eksponen
def hitung_pangkat(bilangan, eksponen):
    hasil = bilangan ** eksponen
    return hasil
# Contoh penggunaan fungsi hitung_pangkat
bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))
hasil = hitung_pangkat(bilangan, eksponen)
print(f"{bilangan}^{eksponen} = {hasil}")
