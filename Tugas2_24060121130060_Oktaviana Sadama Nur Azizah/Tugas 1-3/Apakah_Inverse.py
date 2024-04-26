# Nama file: Elemen_ke_N.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 28 Oktober 2021
# Deskripsi: Mengetahui apakah list L2 merupakan invers dari list L1

# Definisi dan Spesifikasi
# IsInverse : 2 List --> boolean
#   {IsInverse(L1,L2) true jika L2 adalah list dnegan urutan elemen terbalik dibandingkan L1,
# atau hasil invers dari L1}
#
# is_empty : List --> boolean
#   {is_empty(L) bernilai True apabila list L kosong}
#
# first_element : List != [] --> elemen
#   {first_element(L) menghasilkan elemen pertama list L atau L[0]}
#
# last_element : List != [] --> elemen
#   {last_element(L) menghasilkan elemen terakhir list L}
#
# tail_element : List != [] --> elemen
#   {tail_element(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong}
#
# NB_element : List --> integer
#   {NB_element(L) menghasilkan output berupa banyaknya elemen dalam list, nol jika list kosong}
#
# konsi : elemen, List --> List
#   {konsi(S,L) menghasilkan sebuah list dari S dan L, dengan S sebagai elemen terakhir}

# Realisasi
def is_empty(L):
    if L == []:
        return True
    else:
        return False

def first_element(L):
    if not (is_empty(L)):
        return L[0]

def last_element(L):
    if not (is_empty(L)):
        return L[-1]

def tail_element(L):
    if not (is_empty(L)):
        return L[1:]

def head_element(L):
    if not (is_empty(L)):
        return L[:-1]

def NB_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NB_element(tail_element(L))

def IsInverse(L1,L2):
    if (NB_element(L1)) == (NB_element(L2)):
        if is_empty(L1) and is_empty(L2):
            return True
        else:
            return (first_element(L1) == last_element(L2)) and IsInverse(head_element(tail_element(L1)),head_element(tail_element(L2)))
    else: # NB_element(L1) != NB_element(L2)
        return False

L1 = [1,2]
L2 = [2,1]
L3 = [6,-4,2,9]
L4 = [9,-4,2,6]

# Aplikasi
print(IsInverse(L1,L2))
print(IsInverse(L3,L4))
