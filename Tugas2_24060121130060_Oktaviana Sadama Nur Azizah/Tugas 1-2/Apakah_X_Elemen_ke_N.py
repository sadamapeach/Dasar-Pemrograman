# Nama file: Apakah_X_Elemen_ke_N.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 28 Oktober 2021
# Deskripsi: Mengetahui apakah x merupakan elemen ke-N dalam list L

# Definisi dan Spesifikasi
# IsXElmtKeN : elemen, integer, List != [] --> boolean
#   {IsXElmtKeN(x,N,L) bernilai True jika x adalah elemen ke-N list L
#
# is_empty : List --> boolean
#   {is_empty(L) bernilai True apabila list L kosong}
#
# first_element : List != [] --> elemen
#   {first_element(L) menghasilkan elemen pertama list L atau L[0]
#
# tail_element : List != [] --> elemen
#   {tail_element(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong}
#
# is_member : elemen, List --> boolean
#   {is_member(x,L) bernilai True jika x adalah elemen dari list L}
#
# prec : integer --> integer
#   {prec(N) membentuk deret bilangan integer negatif}

# Realisasi
def is_empty(L):
    if L == []:
        return True
    else:
        return False

def first_element(L):
    if not is_empty(L):
        return L[0]

def tail_element(L):
    if not (is_empty(L)):
        return L[1:]

def is_member(L,x):
    if is_empty(L):
        return False
    else:
        if first_element(L) == x:
            return True
        else:
            return is_member(tail_element(L),x)

def prec(N):
    return N-1

def IsXElmtKeN(x,N,L):
    if is_member(L,x):
        if (N == 1) and (first_element(L) == x):
            return True
        else:
            return IsXElmtKeN(x,prec(N),tail_element(L))
    else:
        return False

L = [2, 7, 9.99, 'abc', 'alien']

# Aplikasi
print(IsXElmtKeN(2,1,L))
print(IsXElmtKeN(100,2,L))
print(IsXElmtKeN('alien',5,L))
