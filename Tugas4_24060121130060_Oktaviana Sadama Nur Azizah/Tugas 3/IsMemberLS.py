# Nama file: IsMemberLS.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 9 November 2021
# Deskripsi: Mengecek keanggotaan sebuah list terhadap List of List

# Definisi dan Spesifikasi
# is_empty_LoL : List of List --> boolean
#   {is_empty_LoL(S) bernilai benar jika S adalah List of List kosong}
# Realisasi
def is_empty_LoL(S):
    if S == []:
        return True
    else:
        return False

# first_List : List of List tidak kosong --> List
#   {first_List(S) menghasilkan elemen pertama list, mungkin sebuah list
# atau atom}
# Realisasi
def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

# tail_List : List of List tidak kosong --> List of List
#   {tail_List(S) menghasilkan sisa list of list S tanpa elemen pertama
# list S}
# Realisasi
def tail_List(S):
    if not(is_empty_LoL(S)):
        return S[1:]

# is_atom : List of List --> boolean
#   {is_atom(e) menghasilkan true jika list adalah atom}
# Realisasi
def is_atom(e):
    if(type(e) != list):
        return True
    else:
        return False
    
# Definisi dan Spesifikasi untuk is_equal(L1,L2)
# is_empty : List --> boolean
#   {is_empty(L) bernilai True apabila list L kosong}
# Realisasi
def is_empty(L):
    if L == []:
        return True
    else:
        return False

# first_element : List != [] --> elemen
#   {first_element(L) menghasilkan elemen pertama list L atau L[0]}
# Realisasi
def first_element(L):
    if not (is_empty(L)):
        return L[0]

# tail_element : List != [] --> elemen
#   {tail_element(L) menghasilkan list tanpa elemen pertama list L,
# mungkin kosong}
# Realisasi
def tail_element(L):
    if not (is_empty(L)):
        return L[1:]

# is_equal : 2 List --> boolean
#   {is_equal(L1,L2) true jika L1 identik dengan L2 (semua elemen sama)}
# Realisasi
def is_equal(L1,L2):
    if is_empty(L1) and is_empty(L2):
        return True
    elif is_empty(L1) and not is_empty(L2):
        return False
    elif is_empty(L2) and not is_empty(L1):
        return False
    elif first_element(L1) == first_element(L2):
        return is_equal(tail_element(L1),tail_element(L2))
    else:
        return False

# IsMemberLS : List, List of List --> boolean
#   {IsMemberLS(L,S) bernilai true jika L adalah anggota S}
# Realisasi
def IsMemberLS(L,S):
    if is_empty(L) and is_empty(S):
        return True
    elif not is_empty(L) and is_empty(S):
        return False
    elif is_empty(L) and not is_empty(S):
        return False
    elif not is_empty(L) and not is_empty(S):
        if (is_atom(first_List(S))):
            return IsMemberLS(L,tail_List(S))
        else:
            if is_equal(L,first_List(S)):
                return True
            else:
                return IsMemberLS(L,tail_List(S))

L1 = [17,10]
L2 = [2002, 4, 101]
S = [[56,8,91],[17,10]]

# Aplikasi
print(IsMemberLS(L1,S))
print(IsMemberLS(L2,S))
