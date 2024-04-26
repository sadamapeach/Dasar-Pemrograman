# Nama file: Elemen_ke_N.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 28 Oktober 2021
# Deskripsi: Mengetahui elemen ke-N dalam sebuah list L

# Definisi dan Spesifikasi
# ElmtKeN : integer, List != [] --> elemen
#   {ElmtKeN(N,L) menghasilkan elemen ke-N list L, dimana N <= banyaknya elemen list}
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
# prec : integer --> integer
#   {prec(N) membentuk deret bilangan integer negatif}

# Realisasi
def is_empty(L):
    if L == []:
        return True
    else:
        return False

def first_element(L):
    if not (is_empty(L)):
        return L[0]

def tail_element(L):
    if not (is_empty(L)):
        return L[1:]

def prec(N):
    return N-1

def ElmtKeN(N,L):
    if N == 1:
        return first_element(L)
    else:
        return ElmtKeN(prec(N),tail_element(L))

L = [2, -7, 9.99, 'abc', 'alien']

# Aplikasi
print(ElmtKeN(2,L))
print(ElmtKeN(3,L))
print(ElmtKeN(5,L))
