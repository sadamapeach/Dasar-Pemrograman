# Nama file: Make_Union.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 2 November 2021
# Deskripsi: Membuat union set H1 dengan set H2

# DEFINISI DAN SPESIFIKASI
# make_union : 2 set --> set
#   {make_union(H1,H2) membuat union H1 dengan H2, yaitu set baru dengan semua
# anggota elemen H1 dan anggota H2}
#
# is_empty : List --> boolean
#   {is_empty(L) bernilai True apabila list L kosong}
#
# first_element : List != [] --> elemen
#   {first_element(L) menghasilkan elemen pertama list L atau L[0]}
#
# tail_element : List != [] --> elemen
#   {tail_element(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong}
#
# konso : elemen, List --> List
#   {konso(S,L) menghasilkan sebuah list dari S dan L, dengan S sebagai elemen pertama}
#
# is_member : elemen, List --> boolean
#   {is_member(x,L) bernilai True jika x adalah elemen dari list L}

# REALISASI
def is_empty(L):
    if L == []:
        return True
    else:
        return False

def first_element(L):
    if is_empty(L):
        return []
    else:
        return L[0]

def tail_element(L):
    if not (is_empty(L)):
        return L[1:]

def konso(S,L):
    if is_empty(L):
        return [S]
    else:
        return [S] + L

def is_member(x,L):
    if (is_empty(L)):
        return False
    else:
        if first_element(L) == x:
            return True
        else:
            return is_member(x,tail_element(L))

def make_union(H1,H2):
    if(is_empty(H1) and is_empty(H2)):
        return []
    elif(not is_empty(H1) and is_empty(H2)):
        return H1
    elif(is_empty(H1) and not is_empty(H2)):
        return H2
    elif(not is_empty(H1) and not is_empty(H2)):
        if(is_member(first_element(H1),H2)):
            return make_union(tail_element(H1),H2)
        else:
            return konso(first_element(H1),make_union(tail_element(H1),H2))

H1 = [0,1,2]
H2 = [3,4,5]
H3 = [1,3,5,7,9]
H4 = [2,4,6,8,10]

print(make_union(H1,H2))
print(make_union(H2,H3))
print(make_union(H3,H4))
