# Nama file: pecahan.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 25 September 2021
# Deskripsi: Membuat fungsi pecahan menggunakan tipe bentukan

# Definisi dan spesifikasi type :
# type pecahan : <n: integer >= 0, d: integer > 0>
#   {<n: integer >= 0, d: integer > 0> n adalah pembilang (numerator) dan d adalah
# penyebut (denumerator). Penyebut sebuah pecahan tidak boleh nol}

# Definisi dan spesifikasi selektor dengan fungsi :
# pemb : pecahan --> integer >= 0
#   {pemb(P) memberikan numerator pembilang n dari pecahan tersebut}
# peny : pecahan --> integer > 0
#   {peny(P) memberikan dunumerator penyebut d dari pecahan tersebut}

# Definisi dan spesifikasi konstruktor :
# MakeP : integer >= 0, integer > 0 --> pecahan
#   {MakeP(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan
# x dan y integer}

# Definisi dan spesifikasi operator terhadap pecahan :
# {Operator Aritmatika Pecahan}
# AddP : 2 pecahan --> pecahan
#   {AddP(P1,P2): menambahkan dua buah pecahan P1 dan P2: 
# n1/d1 + n2/d2 = (n1*d2 + n2*d1) / d1*d2}
# SubP : 2 pecahan --> pecahan
#   {SubP(P1,P2): mengurangkan dua buah pecahan P1 dan P2: 
# n1/d1 - n2/d2 = (n1*d2 - n2*d1) / d1*d2}
# MulP : 2 pecahan --> pecahan
#   {MulP(P1,P2): mengalikan dua buah pecahan P1 dan P2: 
# n1/d1 * n2/d2 = n1*d2 / d1*d2}
# DivP : 2 pecahan --> pecahan
#   {DivP(P1,P2): membagi dua buah pecahan P1 dan P2: 
# (n1/d1) / (n2/d2) = n1*d2 / d1*d2}
# RealP : pecahan --> real
#   {menuliskan bilangan pecahan dalam notasi desimal}

# Definisi dan spesifikasi predikat :
# {Operator Relasional Pecahan}
# IsEqP: 2 pecahan --> boolean
#   {IsEqP(P1,P2) true jika P1 == P2
# Membandingkan apakah dua buah pecahan sama nilainya:
# n1/d1 == n2/d2 jika dan hanya jika n1*d2 == n2*d1}
# IsLtP: 2 pecahan --> boolean
#   {IsLtP(P1,P2) true jika P1 < P2
# Membandingkan dua buah pecahan, apakah P1 lebih kecil nilainya dari P2:
# n1/d1 < n2/d2 jika dan hanya jika n1*d2 < n2*d1}
# IsGtP: 2 pecahan --> boolean
#   {IsGtP(P1,P2) true jika P1 > P2
# Membandingkan dua buah pecahan, apakah P1 lebih besar nilainya dari P2:
# n1/d1 > n2/d2 jika dan hanya jika n1*d2 > n2*d1}


# Realisasi :
class Pecahan:
    def __init__(self, n, d):
        self.pembilang = n
        self.penyebut = d

def pemb(pecahan):
    return pecahan.pembilang
def peny(pecahan):
    return pecahan.penyebut

def MakeP(P1, P2):
    return (P1, P2)
def AddP(P1, P2):
    return ((pemb(P1)*peny(P2) + pemb(P2)*peny(P1))/(peny(P1)*peny(P2)))
def SubP(P1, P2):
    return ((pemb(P1)*peny(P2) - pemb(P2)*peny(P1))/(peny(P1)*peny(P2)))
def MulP(P1, P2):
    return ((pemb(P1)*pemb(P2))/(peny(P1)*peny(P2)))
def DivP(P1, P2):
    return ((pemb(P1)*peny(P2))/(peny(P1)*pemb(P2)))
def RealP(P):
    return (pemb(P)/peny(P))
def IsEqP(P1, P2):
    return (pemb(P1)*peny(P2) == peny(P1)*pemb(P2))
def IsLtP(P1, P2):
    return (pemb(P1)*peny(P2) < peny(P1)*pemb(P2))
def IsGtP(P1, P2):
    return (pemb(P1)*peny(P2) > peny(P1)*pemb(P2))

# Aplikasi :
P1 = Pecahan(3, 5) 
P2 = Pecahan(4, 5)
P = Pecahan(2, 5)

print(MakeP(P1, P2))
print(AddP(P1, P2))
print(SubP(P1, P2))
print(MulP(P1, P2))
print(DivP(P1, P2))
print(RealP(P))
print(IsEqP(P1, P2))
print(IsLtP(P1, P2))
print(IsGtP(P1, P2))