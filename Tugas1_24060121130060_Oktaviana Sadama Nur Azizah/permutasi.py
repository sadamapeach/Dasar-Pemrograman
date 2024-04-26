# Nama file: permutasi.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 21 Oktober 2021
# Deskripsi: Menghitung permutasi dengan 2 masukan

# Definisi dan Spesifikasi
# permutasi : 2 integer >= 0 --> integer >= 0
#   permutasi(n,r) : menghitung permutasi dari n (objek keseluruhan) dan r (objek yang diperlukan)
# dimana n adalah bil. bulat positif dan r adalah bil. bulat positif dengan r <=n

# Realisasi
def permutasi(n,r): 
    if r == 0:
        return 1
    elif r == 1:
        return n
    else:
        return n*permutasi(n-1, r-1)

# Aplikasi
print(permutasi(5,0))
print(permutasi(5,1))
print(permutasi(5,2))
print(permutasi(5,3))
print(permutasi(5,4))
