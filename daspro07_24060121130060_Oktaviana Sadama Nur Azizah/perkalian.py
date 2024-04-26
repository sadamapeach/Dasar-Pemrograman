# Nama file = perkalian.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Membuat fungsi perkalian secara rekursif

# Definsi dan Spesifikasi
# mult: 2 integer --> integer
# mult(x,y) mengalikan dua buah bilangan integer

# Realisasi
def mult(x,y):
	if y == 0:
		return 0
	elif y ==1:
		return x
	else:
		return mult(x,y-1) + x

# Aplikasi
print(mult(2,0))
print(mult(3,1))
print(mult(7,5))
print(mult(11,12))
print(mult(20,20))