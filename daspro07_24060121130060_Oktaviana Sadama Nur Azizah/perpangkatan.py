# Nama file = perpangkatan.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Membuat fungsi pangkat secara rekursif

# Definsi dan Spesifikasi
# pangkat: 2 integer --> integer
# pangkat(x,y) memangkatkan sebuah bilangan integer dengan pangkat integer

# Realisasi
def pangkat(x,y):
	if y == 0:
		return 1
	elif y == 1:
		return x
	else:
		return pangkat(x,y-1) * x

# Aplikasi
print(pangkat(2,8))
print(pangkat(5,3))
print(pangkat(10,4))