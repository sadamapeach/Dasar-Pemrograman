# Nama file = pembagian.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Membuat fungsi pembagian secara rekursif

# Definsi dan Spesifikasi
# divs: 2 integer --> integer
# divs(x,y) membagi dua buah bilangan integer dimana x adalah pembilang
# sedangkan y adalah penyebut

# Realisasi
def divs(x,y):
	if x < y:
		return 0
	else:
		return 1 + divs(x-y,y)

# Aplikasi
print(divs(6,3))
print(divs(12,4))
print(divs(25,5))