#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori
#produk berdasarkan penjualan:
#• Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
#• Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
#• Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

def kategorikan_produk(penjualan):
    if penjualan > 1000:
        return "Produk Terlaris"
    elif penjualan >= 500:
        return "Produk Populer"
    else:
        return "Produk Biasa"

def main():
    penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))
    kategori = kategorikan_produk(penjualan)
    
    print(f"Kategori produk: {kategori}")

if __name__ == "__main__":
    main()








