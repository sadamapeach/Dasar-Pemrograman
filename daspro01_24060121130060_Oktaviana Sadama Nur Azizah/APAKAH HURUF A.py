# Nama file: APAKAH HURUF A.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 3 September 2021
# Deskripsi: sebuah predikat yang menerima sebuah karakter dan bernilai benar
#            jika karakter tersebut adalah huruf 'A'

# Deskripsi dan spesifikasi dari fungsi APAKAH HURUF A bernama IsAnA?(C) adalah:
# IsAnA : character --> boolean
#   {IsAnA(C) benar jika C adalah karakter (huruf) 'A'}

# Realisasi
def IsAnA(C):
    return C == 'A'

# Aplikasi
print (IsAnA(1))
print (IsAnA(0))
print (IsAnA(-1))
