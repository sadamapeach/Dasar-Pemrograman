# Nama file = deret_aritmatika.py
# Pembuat = Oktaviana Sadama Nur Azizah
# Tanggal = 22 Oktober 2021
# Deskripsi = Menghitung deret aritmatika secara rekursif

# Definsi dan Spesifikasi
# deret_arit: integer >= 0 --> integer >= 0
# deret_arit(x) menghitung penjumlahan deret 3 kali n

# Realisasi
def deret_arit(x):
	if x == 1:
		return 3
	else:
		return deret_arit(x-1) + 3*x

# Aplikasi
print(deret_arit(1))
print(deret_arit(2))
print(deret_arit(3))