# Nama file: Segitiga_sama_kaki.py
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 10 September 2021
# Deskripsi : Mengecek apakah segitiga merupakan segitiga sama kaki

# Definisi dan spesifikasi :
# segitiga_sama_kaki : integer, integer, integer --> boolean
#   { segitiga_sama_kaki(x,y,z) benar jika nilai (x == y) atau (x == z)
# atau (y == z) }

# Realisasi :
def segitiga_sama_kaki(a,b,c):
    if (a==b==c):
        return False
    else:
        return (a==b or a==c or b==c) 

# Aplikasi :
print(segitiga_sama_kaki(3,3,5))
print(segitiga_sama_kaki(13,14,15))
print(segitiga_sama_kaki(17,9,9))
print(segitiga_sama_kaki(9,9,9))
print(segitiga_sama_kaki(1,2,1))