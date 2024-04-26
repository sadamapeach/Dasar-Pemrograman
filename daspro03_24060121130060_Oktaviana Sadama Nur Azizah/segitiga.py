# Nama file: segitiga.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 19 September 2021
# Deskripsi: Mengetahui macam-macam segitiga berdasarkan panjang sisinya

# Definisi dan spesifikasi :
# segitiga : 3 integer > 0 --> string
#   {segitiga(a,b,c) mengetahui macam-macam segitiga berdasarkan panjang sisinya}

# Realisasi :
def segitiga(a,b,c):
    if (a == b and a == c and b == c):
        return "segitiga sama sisi"
    elif (a == b or a == c or b == c):
        return "segitiga sama kaki"
    else: # (a != b) and (a != c) and (b != c)
        return "segitiga sembarang"

# Aplikasi :
print(segitiga(7,8,9))
print(segitiga(3,3,5))
print(segitiga(17,17,17))
