# Nama file: Segitiga_sembarang.py
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 10 September 2021
# Deskripsi : Mengecek apakah segitiga merupakan segitiga sembarang

# Definisi dan spesifikasi :
# segitiga_sembarang : integer, integer, integer --> boolean
#   { segitiga_sembarang(p,q,r) benar jika nilai (p != q) dan (p != r)
# dan (q != r) }

# Realisasi :
def segitiga_sembarang(p,q,r):
    return (p != q) and (p != r) and (q != r)

# Aplikasi :
print(segitiga_sembarang(8,8,6))
print(segitiga_sembarang(7,8,9))
print(segitiga_sembarang(15,24,15))
