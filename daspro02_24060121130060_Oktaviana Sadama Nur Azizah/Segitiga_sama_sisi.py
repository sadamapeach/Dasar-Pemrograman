# Nama file: Segitiga_sama_sisi.py
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 10 September 2021
# Deskripsi : Mengecek apakah segitiga merupakan segitiga sama sisi

# Definisi dan spesifikasi :
# segitiga_sama_sisi : integer, integer, integer --> boolean
#   { segitiga_sama_sisi(a,b,c) benar jika nilai a == b == c }

# Realisasi :
def segitiga_sama_sisi(a,b,c):
    if a>0 and b>0 and c>0:
        return(a == b == c)
    else:
        return False

# Aplikasi :
print(segitiga_sama_sisi(7,7,9))
print(segitiga_sama_sisi(-5,-5,-5))
print(segitiga_sama_sisi(3,5,3))
print(segitiga_sama_sisi(3,3,3))