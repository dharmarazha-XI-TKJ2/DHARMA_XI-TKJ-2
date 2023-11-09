# NAMA : MOCHAMMAD DHARMA R S
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
# batas tertentu yang ditentukan pengguna.
# Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)
def total_deret_ganjil(batas):
    total = 0
    for i in range(1, 2 * batas, 2):
        total += i
    return total
#Menggunakan fungsi untuk menghitung total deret bilangan ganjil hingga batas tertentu
batas = int(input("Masukkan batas deret bilangan ganjil: "))
hasil = total_deret_ganjil(batas)
print("Total deret bilangan ganjil hingga batas", batas, "adalah", hasil)
