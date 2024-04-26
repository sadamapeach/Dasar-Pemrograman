# Nama file: Max.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 9 November 2021
# Deskripsi: Menentukan nilai maksimum dari List of List

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

# NB_element : List of List --> integer
#   {NB_element(S) menghasilkan banyaknya elemen dalam list of list S}
# Realisasi
def NB_element(S):
    if is_empty_LoL(S):
        return 0
    else:        
        return 1 + NB_element(tail_List(S))

# is_atom : List of List --> boolean
#   {is_atom(e) menghasilkan true jika list adalah atom}
# Realisasi
def is_atom(e):
    if(type(e) != list):
        return True
    else:
        return False

# max2 : 2 integer --> integer
#   {max2(a,b) menghasilkan nilai maksimum a dan b}
# Realisasi
def max2(a,b):
    if a >= b:
        return a
    else:
        return b

# IsOneElmt : List of List --> boolean
#   {IsOneElmt(S) bernilai True jika List of List berisi 1 elemen}
# Realisasi
def IsOneElmt(S):
    if not is_empty_LoL(S):
        return NB_element(S) == 1

# Max : List of List tidak kosong --> integer
#   {Max(S) menghasilkan nilai elemen (atom) yang maksimum dari S}
# Realisasi
def Max(S):
    if IsOneElmt(S):
        if is_atom(first_List(S)):
            return first_List(S)
        else:
            return Max(first_List(S))
    else:
        if is_atom(first_List(S)):
            return max2(first_List(S), Max(tail_List(S)))
        else:
            return max2(Max(first_List(S)),Max(tail_List(S)))

S = [[1],[2,35],[78,99,101]]

# Aplikasi
print(Max(S))
