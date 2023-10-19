#nama   :MOCHAMMAD DHARMA R S
#kelas  :XI TKJ 2
#no absen: 17
#soal buat program python yang memeriksa apakah suatu file sudah ada direktori server. 

#nama file yang ingin diperiksa
nama_file = input ("masukkan nama file: ")

#daftar file yang ada diserver
daftar_file_di_server = ["file1.txt", "file2.txt", "data.txt", "file3.txt"]

#memeriksa apakah nama file sudah di daftar_file_di_server
if nama_file in daftar_file_di_server:
    print("file sudah ada")
else:
    print("file belum ada")







