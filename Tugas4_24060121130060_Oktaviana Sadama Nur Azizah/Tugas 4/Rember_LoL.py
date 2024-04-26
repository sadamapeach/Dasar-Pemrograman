# Nama file: Rember_LoL.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 9 November 2021
# Deskripsi: Menghapus sebuah elemen atom dari List of List

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

# is_List : List of List --> boolean
#   {is_List(e) menghasilkan true jika e adalah sebuah list (bukan atom)}
# Realisasi
def is_List(e):
    if(type(e) == list):
        return True
    else:
        return False

# konso_LoL : List, List of List --> List of List
#   {konso_LoL(L,S) membentuk list baru dengan list yang diberikan sebagai elemen
# pertama list of list}
# Realisasi
def konso_LoL(L,S):
    if is_empty_LoL(S):
        return [L]
    else:
        return [L] + S

# Rember_LoL : elemen, List of List --> List of List
#   {Rember_LoL(a,S) menghapus sebuah elemen bernilai a dari semua list S}
# Realisasi
def Rember_LoL(a, S):
    if(is_empty_LoL(S)):
        return S
    else:
        if(is_List(first_List(S))):
            return konso_LoL(Rember_LoL(a, first_List(S)), Rember_LoL(a, tail_List(S)))
        else:
            if(first_List(S) == a):
                return Rember_LoL(a, tail_List(S))
            else:
                return konso_LoL(first_List(S), Rember_LoL(a, tail_List(S)))

S = [10, [1,2,3], [99,3], 7, 8, 3]

# Aplikasi
print(Rember_LoL(3,S))
