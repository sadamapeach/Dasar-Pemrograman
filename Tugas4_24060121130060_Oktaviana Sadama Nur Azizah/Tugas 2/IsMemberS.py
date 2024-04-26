# Nama file: IsMemberS.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 9 November 2021
# Deskripsi: Mengecek keanggotaan sebuah elemen terhadap list of list

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

# is_List : List of List --> boolean
#   {is_List(e) menghasilkan true jika S adalah sebuah list (bukan atom)}
# Realisasi
def is_List(e):
    if(type(e) == list):
        return True
    else:
        return False

# is_member : elemen, List --> boolean
#   {is_member(x,L) bernilai True jika x adalah elemen dari list L}
# Realisasi
def is_member(x,L):
    if is_empty_LoL(L):
        return False
    elif first_List(L) == x:
        return True
    else:
        return is_member(x,tail_List(L))

# IsMemberS : elemen, List of List --> boolean
#   {IsMemberS(e,S) bernilai true jika e adalah anggota S}
# Realisasi
def IsMemberS(e,S):
    if is_empty_LoL(S):
        return False
    elif not is_empty_LoL(S):
        if is_atom(first_List(S)):
            return e == first_List(S) or IsMemberS(e,tail_List(S))
        elif is_List(first_List(S)):
            return is_member(e,first_List(S)) or is_member(e,tail_List(S))

S = [1, [28,21,37,97], 'abc123']

# Aplikasi
print(IsMemberS(99,S))
print(IsMemberS(97,S))
