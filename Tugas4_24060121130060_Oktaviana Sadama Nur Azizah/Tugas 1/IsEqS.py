# Nama file: IsEqS.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 12 November 2021
# Deskripsi: Mengecek kesamaan dua buah list of list

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
#   {first_List(S) menghasilkan elemen pertama list, mungkin sebuah list atau atom}
# Realisasi
def first_List(S):
    if not(is_empty_LoL(S)):
        return S[0]

# tail_List : List of List tidak kosong --> List of List
#   {tail_List(S) menghasilkan sisa list of list S tanpa elemen pertama list S}
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

# is_List : List of List --> boolean
#   {is_List(e) menghasilkan true jika e adalah sebuah list (bukan atom)}
# Realisasi
def is_List(e):
    if(type(e) == list):
        return True
    else:
        return False

# IsEqS : 2 List of List --> boolean
#   {IsEqS(L1,L2) true jika L1 identik dengan L2 (semua elemen sama)}
# Realisasi
def IsEqS(L1,L2):
    if is_empty_LoL(L1) and is_empty_LoL(L2):
        return True
    elif not is_empty_LoL(L1) and is_empty_LoL(L2):
        return False
    elif is_empty_LoL(L1) and not is_empty_LoL(L2):
        return False
    elif not is_empty_LoL(L1) and not is_empty_LoL(L2):
        if is_atom(first_List(L1)) and is_atom(first_List(L2)):
            return first_List(L1) == first_List(L2) and IsEqS(tail_List(L1),tail_List(L2))
        elif is_List(first_List(L1)) and is_List(first_List(L2)):
            return IsEqS(first_List(L1),first_List(L2)) and IsEqS(tail_List(L1),tail_List(L2))
        else:
            return False

L1 = [99,[2,3],86]
L2 = [99,[2,3],86]
L3 = [1, [7,9,8],15]

# Aplikasi
print(IsEqS(L1,L2))
print(IsEqS(L1,L3))
