# Nama file: Menghitung_jumlah_detik_v2.py
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 10 September 2021
# Deskripsi : Menghitung jumlah detik dengan ketentuan 'am' atau 'pm' dari jam yang terhitung
#             mulai jam 00:00:00 tanggal yang bersangkutan

# Definisi dan spesifikasi :
# menghitung_jumlah_detik : integer [0..11], integer [0..59], integer [0..59],
# string --> integer
# { menghitung_jumlah_detik(j,m,s,k) yaitu menjumlahkan fungsi jam(j) + menit(m) + detik(s)
# dengan ketentuan 'am' atau 'pm' }

# Realisasi :
def menghitung_jumlah_detik(j,m,s,k):
    if (k == "am"):
        return((j*3600) + (m*60) + (s))
    else:
        return(((j+12)*3600) + (m*60) + (s))

# Aplikasi :
print(menghitung_jumlah_detik(8,9,10,"am"))
print(menghitung_jumlah_detik(11,33,16,"pm"))
print(menghitung_jumlah_detik(3,45,28,"am"))
