# Nama file: wujud_air.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 19 September 2021
# Deskripsi: Mengetahui wujud air berdasarkan temperaturnya

# Definisi dan spesifikasi :
# wujud : integer --> string
#   {wujud(c) mengetahui wujud air berdasarkan temperatur derajat celcius}

# Realisasi :
def wujud(c):
    if (c <= 0):
        return "padat"
    elif (0 < c < 100):
        return "cair"
    else: # c >= 100
        return "uap"

# Aplikasi :
print(wujud(-10))
print(wujud(50))
print(wujud(150))
