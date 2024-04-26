# Nama file = pengurangan.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Membuat fungsi pengurangan secara rekursif

# Definsi dan Spesifikasi
# minus : 2 integer --> integer
# minus(x,y) mengurangkan dua buah bilangan integer

# Realisasi
def minus(x,y):
	if y == 0:
		return x
	else:
		return minus(x,y-1) - 1

# Aplikasi
print(minus(7,4))
print(minus(10,5))
print(minus(100,99))