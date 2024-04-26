# Nama file: Menghitung_jumlah_detik_v1.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 10 September 2021
# Deskripsi: Menghitung jumlah detik dari jam yang terhitung mulai jam 00:00:00 tanggal yang
#            bersangkutan menggunakan fungsi antara

# Definisi dan spesifikasi :
# menghitung_jumlah_detik : 3 integer --> integer
#   { menghitung_jumlah_detik(j,m,s) yaitu menjumlahkan fungsi jam(j) + menit(m) + detik(s) }
#
# jam : integer [0..23] --> integer
#   { jam(j) mengubah jam menjadi detik }
#
# menit : integer [0..59] --> integer
#   { menit(m) mengubah menit menjadi detik }
#
# detik : integer [0..59] --> integer
#   { detik(s) memanggil nilai detik }

# Realisasi :
def jam(j):
    return(j*3600)

def menit(m):
    return(m*60)

def detik(s):
    return(s)

def menghitung_jumlah_detik(j,m,s):
    return(jam(j) + menit(m) + detik(s))

# Aplikasi :
print(menghitung_jumlah_detik(17,10,2))
print(menghitung_jumlah_detik(5,33,59))
print(menghitung_jumlah_detik(21,20,21))
