#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan
#apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak
#"Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

def cek_restart_pembaruan():
    pembaruan = input("Apakah ada pembaruan perangkat lunak yang memerlukan restart (y/n)? ").lower()
    
    if pembaruan == "y":
        return "Sistem perlu di-restart."
    elif pembaruan == "n":
        return "Sistem tidak perlu di-restart."
    else:
        return "Input tidak valid. Harap masukkan 'y' atau 'n'."

def main():
    hasil = cek_restart_pembaruan()
    print(hasil)

if __name__ == "__main__":
    main()








