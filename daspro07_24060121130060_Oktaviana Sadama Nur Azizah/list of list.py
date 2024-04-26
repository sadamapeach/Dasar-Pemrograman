def is_empty_LoL(S):
	if S == []:
		return True
	else:
		return False

def first_List(S):
	if not(is_empty_LoL(S)):
		return S[0]

def last_List(S):
	if not(is_empty_LoL(S)):
		return S[-1:]

J = [8,9,2]
print(last_List(J))
 
def tail_List(S):
	if not(is_empty_LoL(S)):
		return S[1:]

def head_List(S):
	if not(is_empty_LoL(S)):
		return S[:-1]
	
def NB_element(S):
	if is_empty_LoL(S):
		return 0
	else:
		return 1 + NB_element(tail_List(S))

def is_atom(e): 
	if(type(e) != list):
		return True
	else:
		return False

def is_List(e):
	if(type(e) == list):
		return True
	else:
		return False

def konso_LoL(L,S):
	if is_empty_LoL(S):
		return [L]
	else:
		return [L] + S

def konsi_LoL(S):
	if is_empty_LoL(S):
		return [L]
	else:
		return S + [L]

#------------------------------------------------------------------------------------------------------
# Soal No.1
L1 = ['i',[2,3],'a']
L2 = ['i',[2,3],'a']

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

print(IsEqS(L1,L2))

# Soal No.2
def is_member(x,L):
	if is_empty_LoL(L):
		return False
	elif first_List(L) == x:
		return True
	else:
		return is_member(x,tail_List(L))

def IsMemberS(e,S):
	if is_empty_LoL(S):
		return False
	elif not is_empty_LoL(S):
		if is_atom(first_List(S)):
			return e == first_List(S) or IsMemberS(e,tail_List(S))
		elif is_List(first_List(S)): # rekursifnya masih salah TT
			return is_member(e,first_List(S)) or is_member(e,tail_List(S))

S = [1, [1,2,3,97], 'abc123']

print(IsMemberS(99,S))

# Soal No.3
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

def is_equal(L1,L2):
	if is_empty(L1) and is_empty(L2):
		return True
	elif is_empty(L1) and not is_empty(L2):
		return False
	elif is_empty(L2) and not is_empty(L1):
		return False
	elif first_element(L1) == first_element(L2):
		return is_equal(tail_element(L1),tail_element(L2))
	else:
		return False

def IsMemberLS(L, S):
    if is_empty(L) and is_empty(S):
        return True
    elif not is_empty(L) and is_empty(S):
        return False
    elif is_empty(L) and not is_empty(S):
        return False
    elif not is_empty(L) and not is_empty(S):
        if is_atom(first_List(S)):
            return IsMemberLS(L, tail_List(S))
        else:
            if is_equal(L,first_List(S)):
                return True
            else:
                return IsMemberLS(L,tail_List(S))

L6 = [17,10]
L7 = [2002,4,101]
P = [[2001,5,100], [17,10]]
print("IsMemberLS----------------------------------------")
print(IsMemberLS(L6,P))
print(IsMemberLS(L7,P))

# Soal No.4
def Rember_LoL(a, S):
    if(is_empty(S)):
        return S
    else:
        if(is_List(first_List(S))):
            return konso_LoL(Rember_LoL(a, first_List(S)), Rember_LoL(a, tail_List(S)))
        else:
            if(first_List(S) == a):
                return Rember_LoL(a, tail_List(S))
            else:
                return konso_LoL(first_List(S), Rember_LoL(a, tail_List(S)))

H = [10, [1,2,3], [99], 7,8]

print(Rember_LoL(3,H))

# Soal No.5
def max2(a,b):
	if a >= b:
		return a
	else:
		return b

def IsOneElmt(S):
	if not is_empty(S):
		return NB_element(S) == 1

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

O = [[1],[2,35],[78,99,101]]

print(Max(O))