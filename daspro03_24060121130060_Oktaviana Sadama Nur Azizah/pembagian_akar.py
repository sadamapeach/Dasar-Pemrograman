# Nama file: pembagian_akar.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 19 September 2021
# Deskripsi: Menghitung hasil pembagian akar persamaan kuadrat menggunakan 
#            rumus abc

# Definisi dan spesifikasi :
# pembagian_akar : 3 integer --> real
#   {pembagian_akar(a,b,c) menghitung hasil pembagian akar persamaan kuadrat
# ax^2 + bx + c = 0}
#
# faktor1 : 3 integer --> integer
#   {faktor1(a,b,c) menghitung 3 masukan integer menggunakan rumus abc +}
#
# faktor2 : 3 integer --> integer
#   {faktor2(a,b,c) menghitung 3 masukan integer menggunakan rumus abc -}
#
# max2 : 2 integer --> integer
#   {max2(x,y) menentukan nilai maximum antara 2 bilangan integer}
#
# min2 : 2 integer --> integer
#   {min2(x,y) menentukan nilai minimum antara 2 bilangan integer}

# Realisasi :
def max2(x,y):
    if (x>y):
        return x
    else: #(x<y)
        return y

def min2(x,y):
    if (x<y):
        return x
    else: #(x>y)
        return y

def faktor1(a,b,c): 
    return (-b + ((b*b - 4*a*c)**0.5)/2*a)
            
def faktor2(a,b,c): 
    return (-b - ((b*b - 4*a*c)**0.5)/2*a)

def pembagian_akar(a,b,c): #contoh pers. kuadrat: f(x)= x^2 - 3x + 2
    return max2(faktor1(a,b,c),faktor2(a,b,c))/min2(faktor1(a,b,c),faktor2(a,b,c))

# Aplikasi :
print(pembagian_akar(1,-3,2))
print(pembagian_akar(1,-3,2))
