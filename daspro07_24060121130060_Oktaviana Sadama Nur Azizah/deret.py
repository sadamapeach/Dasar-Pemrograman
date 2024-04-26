# Nama file = deret.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Menghitung deret secara rekursif

# Definsi dan Spesifikasi
# deret: integer >= 0 --> integer >= 0
# deret(x) menghitung penjumlahan deret integer positif terurut kali dirinya sendiri

# Realisasi
def deret(x):
	if x == 1:
		return 1
	else:
		return deret(x-1) + x*x

# Aplikasi
print(deret(1))
print(deret(2))
print(deret(3))