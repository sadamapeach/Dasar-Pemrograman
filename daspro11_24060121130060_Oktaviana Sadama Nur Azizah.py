# Nama file     : daspro11_24060121130060_Oktaviana Sadama Nur Azizah.py
# Pembuat       : Oktaviana Sadama Nur Azizah
# Tanggal       : 22 November 2021
# Deskripsi     : Binary Tree

def is_empty(S):
    return S == []

def first(S):
    return S[0]

def tail(S):
    return S[1:]

def nb_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def is_member(L,x):
    if is_empty(L):
        return False
    elif first(L) == x:
        return True
    else:
        return is_member(tail(L), x)

def isOne(L):
    if L == 0:
        return False
    elif nb_element(L)==1:
        return True
    else:
        False

def is_list(S):
    if type(S) == list:
        return True
    else:
        return False

#====================================================================
def makePB(root, left, right):
    return [root, left, right]

def root(P):
    return P[0]

def left(P):
    return P[1]

def right(P):
    return P[2]

def istreeEmpty(P):
    if P == None:
        return True
    else:
        return False

def isOneElmt(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False
    
def isUnerLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False

def isUnerRight(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def isbiner(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else: 
        return False

def isExistLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)):
        return True
    else:
        return False

def isExistRight(P):
    if not istreeEmpty(P) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def NbElmt(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1 
    else:
        if isbiner(P):
            return NbElmt(left(P)) + 1 + NbElmt(right(P))
        elif isUnerLeft(P):
            return NbElmt(left(P)) + 1
        elif isUnerRight(P):
            return 1 + NbElmt(right(P))
        else:
            return 0

def repPrefix(P):
    if isOneElmt(P):
        return [root(P)]
    else:
        if isbiner(P):
            return [root(P)] + [repPrefix(left(P))] + [repPrefix(right(P))]
        elif isUnerLeft(P):
            return [root(P)] + [repPrefix(left(P))]
        elif isUnerRight(P):
            return [root(P)] + [repPrefix(right(P))]

def NbDaun(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1
    else:
        if isbiner(P):
            return NbDaun(left(P)) + NbDaun(right(P))
        elif isUnerLeft(P):
            return NbDaun(left(P))
        elif isUnerRight(P):
            return NbDaun(right(P))
        else:
            return 0

# AddX(P,x) : binSearchTree, elemen --> pohonbiner
# {AddX (P,x) menghasilkan sebuah pohon binary search tree P dengan tambahan simpul X, belum ada simpul P yang bernilai X}   
def AddX(P,x):
    if istreeEmpty(P):
        return makePB(x, None, None)
    else:
        if root(P) > x:
            return makePB(root(P), AddX(left(P), x), right(P))
        else:
            return makePB(root(P), left(P), AddX(right(P), x))

# BSearch : binSearchTree, element --> boolean
# {BSearch(P,x) mengirimkan true jika ada node dari pohon binary search tree P yang bernilai X, mengirimkan false jika tidak ada}
def BSearch(P, x):
    if root(P) == x:
        return True
    elif istreeEmpty(P):
        return False
    else:
        if isOneElmt(P):
            return root(P) == x
        else:
            if root(P) < x:
                return BSearch(right(P), x)
            else:
                return BSearch(left(P), x)

# makebintree : list of element --> pohon biner
# {makebintree(L) menghasilkan sebuah pohon binary search tree P yang elemennya berasal dari elemen list L yang dijamin unik }
def BinSearchTree(L,P): #Fungsi tambahan
    if is_empty(L):
        return P
    else :
        return BinSearchTree(tail(L), AddX(P, first(L)))

def makebintree(L):
    return BinSearchTree(L, None)

# delBtree : binsearchtree tidak kosong, elemen --> pohon biner
# {delBtree(P,x) menghasilkan sebuah pohon binary search tree p tanpa node yang bernilai x, x pasti ada sebagai salah satu node, tree menghasilkan tree kosong jika p hanya terdiri dari x}        
def delBtree(P, x):
    if isOneElmt(P):
        if root(P) == x:
            return None
        else:
            return P
    else:
        if isbiner(P):
            if root(P) == x:
                return makePB(root(left(P)), left(left(P)), right(P))
            else:
                return makePB(root(P), delBtree(left(P), x), delBtree(right(P), x))
        elif isUnerLeft(P):
            if root(P) == x:
                return makePB(root(left(P)), left(left(P)), right(P))
            else:
                return makePB(root(P), delBtree(left(P), x), right(P))
        elif isUnerRight(P):
            if root(P) == x:
                return makePB(root(right(P)), left(P), right(right(P)))
            else:
                return makePB(root(P), left(P), delBtree(right(P), x))

# makeBaltree : list of node, integer --> binBaltree
# {makeBaltree(L): menghasilkan sebuah balace tree dengan n node, nilai setiap node yang berasal dari list}
def makeBaltree(L):
    if is_empty(L):
        return None
    else:
        mid=(len(L))//2
        root=L[mid]
        kiri=makeBaltree(L[:mid])
        kanan=makeBaltree(L[mid+1:])
        return makePB(root, kiri, kanan)

# Aplikasi
p0 = makePB(
    2, 
    None, 
    None
)

p1 = makePB(
    5,
    makePB(3, makePB(2,None,None), makePB(4, None, None)),
    makePB(7, makePB(6, None, None), makePB(8,None,None))
)

L1 = [5,3,7,2,6,9]
L2 = [5,3,7,2,6,9,10,54,24,13]

print("AddX :")
print(AddX(p0,1))
print(AddX(p0,7))

print("BSearch :")
print(BSearch(p1,1))
print(BSearch(p1,7))

print("makebintree :")
print(makebintree(L1))
print(makebintree(L2))

print("delBtree :")
print(delBtree(p0,2))
print(delBtree(p1,4))

print("makeBaltree :")
print(makeBaltree(L1))
print(makeBaltree(L2))