#managemen kontak

#list of dictionary
import function


daftar_kontak = []
daftar_kontak.append({
   "nama" : "Erwin",
   "email" : "erwin@yahoo.com",
   "telepon" : "089546934359" 
})

import function
#menu program
while True:
    print("Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Pilih menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")


print("Program selesai berjalan, sampai jumpa")