# Nama file = deret_geometri.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Menghitung deret geometri secara rekursif

# Definsi dan Spesifikasi
# deret_geo: integer >= 0 --> integer >= 0
# deret_geo(x) menghitung penjumlahan deret 3 pangkat n

# Realisasi
def deret_geo(x):
	if x == 1:
		return 1
	else:
		return deret_geo(x-1) + 3**(x-1)

# Aplikasi
print(deret_geo(1))
print(deret_geo(2))
print(deret_geo(3))