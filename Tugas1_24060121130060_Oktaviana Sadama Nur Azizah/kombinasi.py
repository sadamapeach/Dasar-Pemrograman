# Nama file: kombinasi.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 21 Oktober 2021
# Deskripsi: Menghitung kombinasi dengan 2 masukan

# Definisi dan Spesifikasi
# kombinasi : 2 integer >= 0 --> integer >= 0
#   kombinasi(n,r) : menghitung kombinasi dari n (objek keseluruhan) dan r (objek yang diperlukan)
# dimana n adalah bil. bulat positif dan r adalah bil. bulat positif dengan r <=n

# Realisasi
def kombinasi(n,r):
    if r == 0:
        return 1
    elif r == 1:
        return n
    else:
        return (n*kombinasi(n-1, r-1))/r

# Aplikasi
print(kombinasi(3,0))
print(kombinasi(5,1))
print(kombinasi(7,2))
print(kombinasi(10,4))
print(kombinasi(15,5))
