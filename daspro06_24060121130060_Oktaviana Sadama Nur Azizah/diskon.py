# Nama file : diskon.py
# Deskripsi : Mencari harga bersih produk setelah diskon 
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 8 Oktober 2021

def diskon(h,k): 
	if (h > 1000000) and (k == "premium"):
		return (65/100)*h
	elif (h > 1000000 and k == "gold"):
		return (67.5/100)*h
	elif (h > 1000000 and k == "silver"):
		return (70/100)*h

	elif (750000 < h <= 1000000) and (k == "premium"):
		return (75/100)*h
	elif (750000 < h <= 1000000) and (k == "gold"):
		return (77.5/100)*h
	elif (750000 < h <= 1000000) and (k == "silver"):
		return (80/100)*h

	elif (h < 500000) and (k == "premium"):
		return (90/100)*h
	elif (h < 500000) and (k == "gold"):
		return (92.5/100)*h
	elif (h < 500000) and (k == "silver"):
		return (95/100)*h

print(diskon(100000,"premium"))
print(diskon(850000,"silver"))
print(diskon(1200000,"gold"))