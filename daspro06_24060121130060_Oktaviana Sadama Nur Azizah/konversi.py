# Nama file : konversi.py
# Deskripsi : Mengkonversikan decimal menjadi hexadecimal
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 8 Oktober 2021

def IntToChar(x):
    return str(x)

def KonkatStr(s,c):
    return str(x)

def decimal(x):
	return (x//16, x%16), ((x//16)//16, (x//16)%16), (((x//16)//16)//16, (((x//16)//16)%16))

def urutan(x):
	return ((x//16)//16)//16, (((x//16)//16)%16), (x//16)%16, x%16

def KonversiHexadesimal(x):
	if ((x//16)//16)//16 == 10 or (((x//16)//16)%16) == 10 or (x//16)%16 == 10 or x%16 == 10:
		return "A"
	elif ((x//16)//16)//16 == 11 or (((x//16)//16)%16) == 11 or (x//16)%16 == 11 or x%16 == 11:
		return "B"
	elif ((x//16)//16)//16 == 12 or (((x//16)//16)%16) == 12 or (x//16)%16 == 12 or x%16 == 12:
		return "C"
	elif ((x//16)//16)//16 == 13 or (((x//16)//16)%16) == 13 or (x//16)%16 == 13 or x%16 == 13:
		return "D"
	elif ((x//16)//16)//16 == 14 or (((x//16)//16)%16) == 14 or (x//16)%16 == 14 or x%16 == 14:
		return "E"
	elif ((x//16)//16)//16 == 15 or (((x//16)//16)%16) == 15 or (x//16)%16 == 15 or x%16 == 15:
		return "F"

def hexadecimal(x):
	return ((x//16)//16)//16, KonversiHexadesimal(x), (x//16)%16, x%16

# Aplikasi
print(decimal(11600))
print(urutan(11600))
print(hexadecimal(11600))