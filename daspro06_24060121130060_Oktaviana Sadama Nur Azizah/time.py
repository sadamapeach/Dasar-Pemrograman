# Nama file : time.py
# Deskripsi : Menghitung time <j,m,d> apabila ditambah n (integer)
# Pembuat : Oktaviana Sadama Nur Azizah
# Tanggal : 9 Oktober 2021

def make_time(j,m,d):
	return [j,m,d]

def jam(W):
	return W[0]

def menit(W):
	return W[1]

def detik(W):
	return W[2]

def NextNSecond(T,n): 
	if T[2]+n < 60:
		return T[0], T[1], T[2]+n 
	else: # T[2]+n >= 60
		return T[0]+(T[1]+((T[2]+n)//60))-60, (T[1]+((T[2]+n)//60))-60, (T[2]+n)%60

T = make_time(10,20,30)
T1 = make_time(10,59,30)

print(NextNSecond(T,10))
print(NextNSecond(T1,100)) 