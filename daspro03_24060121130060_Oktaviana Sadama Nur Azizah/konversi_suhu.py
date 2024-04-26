# Nama file: konversi_suhu.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 18 September 2021
# Deskripsi: Mengkonversikan derajat celcius ke derajat reamur, fahrenheit, dan kelvin

# Definisi dan spesifikasi :
# konversi : integer, string --> real
#   {konversi(x,ket) mengkonversikan derajat celcius ke derajat reamur, fahrenheit, atau
# kelvin}

# Realisasi :
def konversi(x, ket):
    if (ket == "r"):
        return x*(4/5)
    elif (ket == "f"):
        return x*(9/5) + 32
    else: #(ket == "k")
        return x+273

# Aplikasi :
print(konversi(40, "r"))
print(konversi(40, "f"))
print(konversi(40, "k"))
