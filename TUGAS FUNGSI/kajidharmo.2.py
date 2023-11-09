# NAMA : MOCHAMMAD DHARMA R S
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.
# Rumus: Faktorial n = n * (n-1) * (n-2) * ... * 1
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

# Contoh penggunaan fungsi faktorial
bilangan = int(input("Masukkan bilangan: "))
hasil = faktorial(bilangan)
print(f"{bilangan}! = {hasil}")
