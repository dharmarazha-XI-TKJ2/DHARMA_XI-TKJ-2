# NAMA : MOCHAMMAD DHARMA R S
# KELAS : XI TKJ 2
# ABSEN : 17
# Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.
# Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Contoh penggunaan fungsi fibonacci
n = int(input("Masukkan nilai n: "))
hasil = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")
