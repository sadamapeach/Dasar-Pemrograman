# Nama file     : daspro12_24060121130060_Oktaviana Sadama Nur Azizah.py
# Pembuat       : Oktaviana Sadama Nur Azizah
# Tanggal       : 27 November 2021
# Deskripsi     : UAS Daspro 2020

def empty_list(L):
	if L == []:
		return True
	else:
		return False

def first_element(L):
	if not empty_list(L):
		return L[0]

def tail(L):
	if not empty_list(L):
		return L[1:]

def konso(e, L):
	if empty_list(L):
		return [e]
	else:
		return [e] + L

def NB_element(L):
	if empty_list(L):
		return 0
	else:
		return 1 + NB_element(tail(L))

def one_element(L):
	if not empty_list(L):
		return NB_element(L) == 1

# Soal No.1
def max2(a, b):
	if a > b:
		return a
	else:
		return b

def min2(a, b):
	if a < b:
		return a
	else:
		return b

def max_list(L):
	if empty_list(L):
		return []
	elif one_element(L):
		return first_element(L)
	else:
		return max2(first_element(L), max_list(tail(L)))

def min_list(L):
	if empty_list(L):
		return []
	elif one_element(L):
		return first_element(L)
	else:
		return min2(first_element(L), min_list(tail(L)))


L1 = [9, 2, 5, 1, 4, -3, 10, -9, 1]

print("max list:", max_list(L1))
print("min list:", min_list(L1))

# Soal No.2
def MakePB(A, L, R):
	return [A, L, R]

def akar(P):
	return P[0]

def left(P):
	return P[1]

def right(P):
	return P[2]

def is_tree_empty(P):
	if P == None:
		return True
	else:
		return False

def is_biner(P):
	if not is_tree_empty(P) and not is_tree_empty(left(P)) and not is_tree_empty(right(P)):
		return True
	else:
		return False

def is_uner_left(P):
	if not is_tree_empty(P) and not is_tree_empty(left(P)) and is_tree_empty(right(P)):
		return True
	else:
		return False

def is_uner_right(P):
	if not is_tree_empty(P) and is_tree_empty(left(P)) and not is_tree_empty(right(P)):
		return True
	else:
		return False

def is_one_element(P):
	if not is_tree_empty(P) and is_tree_empty(left(P)) and is_tree_empty(right(P)):
		return True
	else:
		return False

def total_element_daun(P):
	if is_one_element(P):
		return akar(P)
	else:
		if is_biner(P):
			return total_element_daun(left(P)) + total_element_daun(right(P))
		elif is_uner_left(P):
			return total_element_daun(left(P))
		elif is_uner_right(P):
			return total_element_daun(right(P))

def NB_daun(P):
	if is_one_element(P):
		return 1
	else:
		if is_biner(P):
			return NB_daun(left(P)) + NB_daun(right(P))
		elif is_uner_left(P):
			return NB_daun(left(P))
		elif is_uner_right(P):
			return NB_daun(right(P))

def max_elemen_daun(P):
	if is_one_element(P):
		return akar(P)
	else:
		if is_biner(P):
			return max2(max_elemen_daun(left(P)), max_elemen_daun(right(P)))
		elif is_uner_left(P):
			return max_elemen_daun(left(P))
		elif is_uner_right(P):
			return max_elemen_daun(right(P))


def total_element_node(P):
	if is_one_element(P):
		return akar(P)
	else:
		if(is_biner(P)):
			return total_element_node(left(P)) + akar(P) + total_element_node(right(P))
		elif(is_uner_left(P)):
			return total_element_node(left(P)) + akar(P)
		elif(is_uner_right(P)):
			return akar(P) + total_element_node(right(P))

def NB_node(P):
	if is_one_element(P):
		return 1
	else:
		if(is_biner(P)):
			return NB_node(left(P)) + 1 + NB_node(right(P))
		elif(is_uner_left(P)):
			return NB_node(left(P)) + 1
		elif(is_uner_right(P)):
			return 1 + NB_node(right(P))

def rata2_elemen_node(P):
	return total_element_node(P) / NB_node(P)

def BST(a, P):
	if(akar(P) == a):
		return True
	elif(is_tree_empty(P)):
		return False
	else:
		if(is_one_element(P)):
			if(akar(P) == a):
				return True
			else:
				return False
		else:
			if(akar(P) < a):
				return BST(a, right(P))
			else:
				return BST(a, left(P))

# Tree
#					8
#				  /   \
#				 3     10
#			    / \      \
#			   1   6     14
#				  / \    /
#                4   7  13
P = MakePB(8, MakePB(3, MakePB(1, None, None), MakePB(6, MakePB(4, None, None), 
	MakePB(7, None, None))), MakePB(10, None, MakePB(14, MakePB(13, None, None), None)))

# Tree
#				   50
#				/      \
#			   17      72
#			 /   \    /  \
#			12    23 54  76
#		   /  \	  /   \
#         9   14 19    67
P1 = MakePB(50, MakePB(17, MakePB(12, MakePB(9, None, None), MakePB(14, None, None)), MakePB(23, MakePB(19, None, None), None)), 
	 MakePB(72, MakePB(54, None, MakePB(67, None, None)), MakePB(76, None, None)))
	
print("total elemen daun:", total_element_daun(P1))
print("NB daun:", NB_daun(P1))
print("max elemen daun:", max_elemen_daun(P1))
print("total elemen node:", total_element_node(P1))
print("NB node:", NB_node(P1))
print("rata rata:", rata2_elemen_node(P1))
print("BST:", BST(7, P1))

# Soal No.3
def kelipatan10(x):
	if x % 10 == 0:
		return True
	else:
		return False

def bukan_kelipatan10(x):
	if x % 10 != 0:
		return True 
	else:
		return False

def Filter_List(L, x):
	if empty_list(L):
		return []
	elif not (x(first_element(L))):
		return Filter_List(tail(L), x)
	else:
		return konso(first_element(L), Filter_List(tail(L), x))

L1 = [40, 8, 11, 20, 19, 23, 30]
L2 = Filter_List(L1, lambda x: x % 10 == 0)
L3 = Filter_List(L1, lambda x: x % 10 != 0)

print("kelipatan 10:", L2)
print("bukan kelipatan 10:", L3)

# Soal No.4
def is_member(x, L):
	if empty_list(L):
		return False
	elif first_element(L) == x:
		return True
	else:
		return is_member(x, tail(L))

def is_sub_set(L1, L2):
	if empty_list(L1):
		return True
	elif not is_member(first_element(L1), L2):
		return False
	else:
		return is_sub_set(tail(L1), L2)

def minus(L1, L2):
	if empty_list(L1):
		return []
	elif empty_list(L2):
		return L1
	else:
		if is_member(first_element(L1), L2):
			return minus(tail(L1), L2)
		else:
			return konso(first_element(L1), minus(tail(L1), L2))

A = [5, 2, 6, 7, 9, 15]
B = [2, 7, 15]

print("minus:", minus(A, B))