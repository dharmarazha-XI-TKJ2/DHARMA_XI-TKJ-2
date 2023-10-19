#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis
#pinjaman berdasarkan aturan berikut:

#• Peminjaman 7 hari atau kurang: "Peminjaman Pendek"
#• Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah"
#• Peminjaman lebih dari 30 hari: "Peminjaman Panjang"

def tentukan_jenis_pinjaman(durasi_peminjaman):
    if durasi_peminjaman <= 7:
        return "Peminjaman Pendek"
    elif durasi_peminjaman > 7 and durasi_peminjaman <= 30:
        return "Peminjaman Menengah"
    else:
        return "Peminjaman Panjang"

def main():
    durasi_peminjaman = int(input("Masukkan durasi peminjaman buku dalam hari: "))
    jenis_pinjaman = tentukan_jenis_pinjaman(durasi_peminjaman)
    
    print(f"Jenis pinjaman: {jenis_pinjaman}")

if __name__ == "__main__":
    main()






