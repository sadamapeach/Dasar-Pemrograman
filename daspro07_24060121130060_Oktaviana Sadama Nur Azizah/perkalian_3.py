# Nama file = perkalian_3.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Menghitung perkalian suatu bilangan dengan 3 secara rekursif

# Definsi dan Spesifikasi
# mult3: integer --> integer
# mult3(x) mengalikan sebuah bilangan integer dengan 3

# Realisasi
def mult3(x):
	if x == 0:
		return 0
	elif x == 1:
		return 3
	else:
		return mult3(x-1) + 3

# Aplikasi
print(mult3(9))
print(mult3(17))
print(mult3(21))