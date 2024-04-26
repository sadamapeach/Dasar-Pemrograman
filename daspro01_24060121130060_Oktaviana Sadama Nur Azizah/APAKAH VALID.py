# Nama file: APAKAH VALID.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 3 September 2021
# Deskripsi: sebuah predikat yang menerima sebuah besaran integer, dan menentukan
#            apakah bilangan tersebut valid

# Deskripsi dan spesifikasi dari fungsi APAKAH VALID bernama IsValid?(x) adalah:
# IsValid? : integer --> boolean
#   {IsValid?(x) benar jika (x) bernilai lebih kecil dari 5 atau lebih besar dari
#   500}

# Realisasi
def IsValid(x):
    return (x < 5) or (x > 500)

# Aplikasi
print (IsValid(5))
print (IsValid(0))
print (IsValid(500))
print (IsValid(6000))
