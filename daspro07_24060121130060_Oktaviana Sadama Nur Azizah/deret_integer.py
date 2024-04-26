# Nama file = deret_integer.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Menghitung deret bilangan integer secara rekursif

# Definsi dan Spesifikasi
# deret_int: integer >= 0 --> integer >= 0
# deret_int(x) menghitung deret bilangan integer positif secara urut 
# sampai bilangan ke n 

# Realisasi
def deret_int(x):
	if x == 1:
		return 1
	else:
		return deret_int(x-1) + x

# Aplikasi
print(deret_int(3))
print(deret_int(4))
print(deret_int(5))