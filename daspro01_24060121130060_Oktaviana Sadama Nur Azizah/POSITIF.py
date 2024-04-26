# Nama file: POSITIF.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 3 September 2021
# Deskripsi: sebuah predikat yang menerima sebuah bilangan bulat dan bernilai
#            benar jika bilangan tersebut positif

# Deskripsi dan spesifikasi dari fungsi POSITIF bernama IsPositif?(x) adalah:
# IsPositif? : integer --> boolean
#   {IsPositif? (x) benar jika x positif}

# Realisasi
def IsPositif(x):
    return x >= 0

# Aplikasi
print (IsPositif(1))
print (IsPositif(0))
print (IsPositif(-1))
