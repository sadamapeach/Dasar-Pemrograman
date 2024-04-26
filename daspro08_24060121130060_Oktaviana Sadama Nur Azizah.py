# Nama file: Tugas8.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 1 November 2021

def IsEmpty(L):
    return L == []

def FirstElmt(T):
    if not IsEmpty(T):
        return T[0]
    else:
        return []

def LastElmt(L):
    if not IsEmpty(L):
        return L[-1]
    else:
        return []

def Head(L):
    if not IsEmpty(L):
        return L[:-1]
    else:
        return []

def Tail(T):
    if not IsEmpty(T):
        return T[1:]
    else:
        return []

def IsMember(X, L):
    if IsEmpty(L):
        return False
    elif FirstElmt(L) == X:
        return True
    else:
        return IsMember(X, Tail(L))

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def Konso(x, l):
	return [x] + l

def Kons(l, x):
	return l + [x]

def Konsa(x, y, l):
	return [y] + [x] + l

def Rember(l1, l2):
    if IsEmpty(l2):
        return []
    elif FirstElmt(l2) == l1:
        return Tail(l2)
    else:
        return Konso(FirstElmt(l2), Rember(l1, Tail(l2)))

def is_prima(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

# Soal ---------------------------------------------------------------------------------------------------------
# No.1
# DefSpek
# NbVokal : list of char --> integer
# NbVokal(L) menghitung banyak elemen vokal dalam list
# Realisasi
def NbVokal(L):
    vokal = ['a','i','u','e','o']
    if IsEmpty(L):
        return 0
    elif IsMember(FirstElmt(L).lower(),vokal):
        return 1 + NbVokal(Tail(L))
    else:
        return NbVokal(Tail(L))

L = ['s','A','d','a','M','a']

print(NbVokal(L))

# No.2
# SumElmt : list of integer --> integer
# SumElmt(L) menghasilkan jumlah semua elemen dalam list
# Realisasi
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

L = [9, 4, 12, 5, 37, 69, 101]

print(SumElmt(L))

# No.3
# KEMUNCULAN MAKSIMUM versi-2
# maxNb : list of integer --> <integer, integer>
# maxNb(Li) menghasilkan <nilai maksimum, kemunculan nilai maksimum> dari suatu list integer Li; <m,n> = m adalah maks x dari n
#           occurence m dalam list
#
# max : list of integer --> integer
# max(Li) menghasilkan nilai maksimum dari elemen suatu list integer Li
#
# Vmax : list of integer --> integer
# Vmax(Li) adalah NbOcc(max(Li),Li) yaitu banyaknya kemunculan nilai maksimum dari
#          Li, dengan aplikasi terhadap NbOcc(max(Li),Li)
#
# NbOcc : integer, list of integer --> integer > 0
# NbOcc(X,Li) yaitu banyaknya kemunculan nilai X pada Li
# Realisasi
def Max(L):
    return max(L)

def NbOcc(x,L):
    if IsEmpty(L):
        return 0
    elif FirstElmt(L) == x:
        return 1 + NbOcc(x,Tail(L))
    else:
        return NbOcc(x,Tail(L))

def Vmax(L):
    return NbOcc(Max(L),L)

def maxNB(L):
    return Max(L), Vmax(L)

L = [4,6,8,10,10]  

print("maxNB:", maxNB(L))
print("Max:", Max(L))

# No.4
# LPrime(L) : list of integer --> list
# LPrime(L) menghasilkan list baru yang dimana isinya hanya bilangan prima
# Realisasi
def LPrime(L):
    if IsEmpty(L):
        return []
    else:
        if is_prima(FirstElmt(L)) == True:
            return Konso(FirstElmt(L),LPrime(Tail(L)))
        else:
            return LPrime(Tail(L))

L = [11,22,33,44,55]

print(LPrime(L))

# No.5
# InsertAfter: list --> list
# InsertAfter(L,x,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e
# Realisasi
def InsertAfter(L,x,e):
    if IsEmpty(L):
        return [x] + [e]
    else:
        return L + [x] + [e]

L = ['spiderman', 'captain america', 'black widow', 'hulk']

print(InsertAfter(L,'thor','black panther'))

# No.6
# MakeMinus: 2 set --> set
# MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2
# Realisasi
H1 = [1,2,3,4,5]
H2 = [1,3,5]
def MakeMinus(H1,H2):
    if IsEmpty(H1):
        return []
    elif IsEmpty(H2):
        return H1
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeMinus(Tail(H1), H2)
        else:
            return [FirstElmt(H1)] + MakeMinus(Tail(H1),H2)

print(MakeMinus(H1,H2))

# No.7
# MakeKomplemen: 2 set --> set
# MakeKomplemen(H1,H2) membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                      tetapi bukan interseksi keduanya
# Realisasi
H1 = [1,3,5,7]
H2 = [1,1,2,3,3,9]

def ListCombine(L1, L2):
    return L1 + L2

def MakeKomplemen1(H):
    if IsEmpty(H):
        return []
    else:
        if not(IsMember(FirstElmt(H),Tail(H))):
            return [FirstElmt(H)] + MakeKomplemen1(Tail(H))
        else:
            return MakeKomplemen1(Tail(H))

def MakeKomplemen(H1,H2):
    return MakeKomplemen1(ListCombine(H1,H2))

print(MakeKomplemen(H1,H2))