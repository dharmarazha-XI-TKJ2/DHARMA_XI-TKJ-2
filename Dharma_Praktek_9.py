#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek
#tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek
#diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."

def cek_status_persiapan():
    status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ").lower()
    
    if status_persiapan == "siap":
        return "Proyek diluncurkan."
    elif status_persiapan == "tunda":
        return "Proyek ditunda."
    else:
        return "Status persiapan tidak valid. Harap masukkan 'Siap' atau 'Tunda'."

def main():
    hasil = cek_status_persiapan()
    print(hasil)

if __name__ == "__main__":
    main()






