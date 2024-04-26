"""
NIM         : 24060121130060
Nama        : Oktaviana Sadama Nur Azizah
Deskripsi   : List of List
Tanggal     : 14 November 2021
"""
"""Ex:
Matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
Matrix1 = [
              [1,2,3],
              [4,5,6],
              [7,8,9]
              ]
"""
# DEFINISI DAN SPESIFIKASI
# IsEmpty : list of list --> boolean
#   {IsEmpty(L) bernilai benar jika S adalah list of list}
def IsEmpty(L):
    return L == []

# FirstList: List of list tidak kosong --> List
#   {FirstList(T) Menghasilkan elemen pertama list, mungkin sebuah list atau atom}
def FirstList(T):
    if not IsEmpty(T):
        return T[0]
    else:
        return []

# Tail : List of list tidak kosong --> List of list
#   {Tail(T) Menghasilkan "sisa" list of list T tanpa elemen pertama list T}
def Tail(T):
    if not IsEmpty(T):
        return T[1:]
    else:
        return []

# is_atom : list --> boolean
#   {is_atom(e) bernilai benar jika elemen list sebuah atom}
def is_atom(e): 
    if(type(e) != list):
        return True
    else:
        return False

# IsList : List --> boolean
#   {IsList(e) bernilai benar jika elemen list adalah sebuah list}
def is_List(e):
    if(type(e) == list):
        return True
    else:
        return False

# Konso : List, List of list --> List of list
#   {KonsoLoL(L,S) diberikan sebuah List L dan sebuah List of List S, membentuk list baru
# dengan List yang diberikan sebagai elemen pertama List of list: L + S --> S'}
def Konso(L,S):
    if IsEmpty(S):
        return [L]
    else:
        return [L] + S

# ------------------------------------------------ SOAL -----------------------------------------------------
# 1
# DefSpek
# NbEleX : elemen, list of list --> integer
# NbEleX (X,L) menentukan banyaknya X dalam list L
# L1 = [[4], 2, [3,4], 1, 4]
# aplikasi : NbEleX(4,L1) --> 3 
# Realisasi
def NbEleSubX(X, L): # menentukan banyaknya X dalam list L
    if IsEmpty(L) == True:
        return 0
    else:
        if FirstList(L) == X:
            return 1 + NbEleSubX(X, Tail(L))
        else:
            return NbEleSubX(X, Tail(L))

def NbEleX(X, L):
    if IsEmpty(L) == True:
        return 0
    else: 
        if is_atom(FirstList(L)) == True:
            if FirstList(L) == X:
                return 1 + NbEleX(X, Tail(L))
            else:
                return NbEleX(X, Tail(L))
        elif is_List(FirstList(L)) == True:
            return NbEleSubX(X, FirstList(L)) + NbEleX(X, Tail(L))
        else:
            return NbEleX(X, Tail(L))

L1 = [[4], 2, [3,4], 1, 4]
print("NbEleX")
print(NbEleX(4,L1))

# 2
# DefSpek
# KaliMatrix : Integer, list of list dalam bentuk matrix --> list
# KaliMatrix (L, k) menghasilkan matrix dalama bentuk list
# yang telah dikali dengan suatu konstanta K
# L3 = [[1,2,3], [4,5,6], [7,8,9]]
# aplikasi : KaliMatrix(L3, 2) --> [[2,4,6],[8,10,12],[14,16,18]]
# Realisasi
def ElmtMultX(L, x): # mengalikan elemen dalam list L dengan x
    if IsEmpty(L) == True:
        return []
    else: 
        return Konso(FirstList(L)*x, ElmtMultX(Tail(L), x))

def KaliMatrix (L, k):
    if IsEmpty(L) == True:
        return []
    elif is_atom(FirstList(L)) == True:
        return Konso(FirstList(L)*k, KaliMatrix(Tail(L), k))
    else: # is_List(FirstList(L)) == True
        return Konso(ElmtMultX(FirstList(L), k), KaliMatrix(Tail(L), k))

L3 = [[1,2,3], [4,5,6], [7,8,9]]
print("KaliMatrix")
print(KaliMatrix(L3, 2))

# 3
# DefSpek
# NbList : list of list --> integer
# NbList (L) menghitung jumlah list dalam list L
# L7 = [1, [2,3], [4]]
# L8 = [[5], [6], [7]]
# L9 = [8, 9, 10]
# aplikasi : NbList(L7) --> 2
#               NbList(L8) --> 3
#               NbList(L9) --> 0
# Realisasi
def NbList(L):
    if IsEmpty(L) == True:
        return 0
    else:
        if is_List(FirstList(L)) == True:
            return 1 + NbList(Tail(L))
        else:
            return NbList(Tail(L))

L7 = [1, [2,3], [4]]
L8 = [[5], [6], [7]]
L9 = [8, 9, 10]
print("NbList")
print(NbList(L7))
print(NbList(L8))
print(NbList(L9))