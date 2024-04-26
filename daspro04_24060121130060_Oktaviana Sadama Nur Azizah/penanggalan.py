# Nama file: penanggalan.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 25 September 2021
# Deskripsi: Membuat fungsi penaggalan menggunakan tipe bentukan

# Definisi dan spesifikasi type :
# type Hr : integer [1...31]
#   {definisi ini hanyalah untuk "menamakan" type integer dengan nilai tertentu 
# supaya mewakili hari, sehingga jika dipunyai suatu nilai integer, kita dapat
#  memeriksa apakah nilai integer tersebut mewakili Hari yang absah}
# type Bln : integer [1...12]
#   {definisi ini hanyalah untuk "menamakan" type integer dengan daerah nilai 
# tertentu supaya mewakili bulan}
# type Thn : integer > 0
#   {definisi ini hanyalah untuk "menamakan" type integer dengan daerah nilai 
# tertentu supaya mewakili tahun}
# type date <d: Hr, m: Bln, y: Thn>
#   {<d,m,y> adalah tanggal d bulan m tahun y}

# Definisi dan spesifikasi selektor :
# Day : date --> Hr
#   {Day(D) memberikan hari d dari D yang terdiri dari <d,m,y>}
# Month : date --> Bln
#   {Month(D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
# Year : date --> Thn
#   {Year(D) memberikan tahun y dari D yang terdiri dari <d,m,y>}

# Konstruktor :
# MakeDate : <Hr,Bln,Thn> --> date
#   {MakeDate (<h,b,t>) --> tanggal pada hari, bulan, tahun yang bersangkutan}

# Definisi dan spesifikasi operator/fungsi lain terhadap date :
# Nextday : date --> date
#   {NextDay(D): menghitung date yang merupakan keesokan hari dari date D yang
# diberikan:
#               Nextday (<1,1,80>) adalah (<2,1,80>)
#               Nextday (<31,1,80>) adalah (<1,2,80>)
#               Nextday (<30,4,80>) adalah (<1,5,80>)
#               Nextday (<31,12,80>) adalah (<1,1,81>)
#               Nextday (<28,2,80>) adalah (<29,2,80>)
#               Nextday (<28,2,81>) adalah (<1,3,82>) }

# Type Data (lanjutan)
# Yesterday : date --> date
#   {Yesterday(D): menghitung date yang merupakan 1 hari sebelum date D yang 
# diberikan :
#               Yesterday (<1,1,80>) adalah (<31,12,79>)
#               Yesterday (<31,1,80>) adalah (<30,1,80>)
#               Yesterday (<1,5,80>) adalah (<30,4,80>)
#               Yesterday (<31,12,80>) adalah (<30,12,80>)
#               Yesterday (<29,2,80>) adalah (<28,2,80>)
#               Yesterday (<1,3,80>) adalah (<29,2,80>) }
# NextNDay : date, integer --> date
#   {NextNDay(D,N): menghitung date yang merupakan N hari (N adalah nilai integer)
# sesudah dari date D yang diberikan}
# HariKe1900 : date --> integer [0...366]
#   {HariKe1900(D): menghitung jumlah hari terhadap 1 Januari pada tahun y, dengan
# memperhitungkan apakah y adalah tahun kabisat}

# Predikat :
# IsEqD : 2 date --> boolean
#   {IsEqD(d1,d2) benar jika d1 == d2, mengirimkan true jika d1 == d2 and m1 == m2
# and y1 == y2. Contoh:    EqD(<1,1,90>, <1,1,90>) adalah true
#                          EqD(<1,2,90>, <1,1,90>) adalah false}
# IsBefore : 2 date --> boolean
#   {IsBefore(d1,d2) benar jika d1 adalah sebelum d2 mengirimkan true jika D1 adalah
# "sebelum" D2:
# HariKe1900 dari D1 adalah lebih kecil dari HariKe1900 D2
# Contoh: Before (<1,1,80>, <1,2,80>) adalah false
#         Before (<1,1,80>, <2,1,80>) adalah true }
# IsAfter : 2 date --> boolean
#   {IsAfter(d1,d2) benar jika d1 adalah sesudah d2 mengirimkan true jika D1 adalah
# "sesudah" D2:
# HariKe1900 dari D1 adalah lebih besar dari HariKe1900 dari D2
# Contoh: After (<1,11,80>, <1,2,80>) adalah true
#         After (<1,1,80>, <2,1,80>) adalah false
#         After (<1,1,80>, <1,1,80>) adalah false }
# IsKabisat : integer --> boolean
#   {IsKabisat(a) true jika tahun 1900+a adalah tahun kabisat: habis dibagi 4 tetapi
# tidak habis dibagi 100 atau habis dibagi 400}

# Realisasi
class Hr:
    def __init__(self, hari):
        self.hari = hari

class Bln:
    def __init__(self, bulan):
        self.bulan = bulan

class Thn:
    def __init__(self, tahun):
        self.tahun = tahun

class Date(Hr,Bln,Thn):
    def __init__(self, hari, bulan, tahun):
        Hr.__init__(self, hari)
        Bln.__init__(self, bulan)
        Thn.__init__(self, tahun)

def Day(D):
    return D.hari if 1 <= D.hari <= 31 else "False" 

def Month(D):
    return D.bulan if 1 <= D.bulan <= 12 else "False"

def Year(D):
    return D.tahun if D.tahun > 0 else "False"
  
def Nextday(D):
    if Month(D) == 1 or Month(D) == 3 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10: #Bulan dengan 31 hari
        if Day(D) < 31:
            return Date(Day(D)+1, Month(D), Year(D))
        elif Day(D) == 31:
            return Date(1, Month(D)+1, Year(D))
    elif Month(D) == 2: #Februari
        if IsKabisat(D) == True:
            if Day(D) < 29:
                return Date(Day(D)+1, Month(D), Year(D))
            elif Day(D) == 29:
                return Date(1, Month(D)+1, Year(D))
        else:
            if Day(D) < 28:
                return Date(Day(D)+1, Month(D), Year(D))
            elif Day(D) == 28:
                return Date(1, Month(D)+1, Year(D))
    elif Month(D) == 4 or Month(D) == 6 or Month(D) == 9 or Month(D) == 11: #Bulan dengan 30 hari
        if Day(D) < 30:
            return Date(Day(D)+1, Month(D), Year(D))
        elif Day(D) == 30:
            return Date(1, Month(D)+1, Year(D))
    elif Month(D) == 12: #Desember
         if Day(D) < 31:
            return Date(Day(D)+1, Month(D), Year(D))
    elif Day(D) == 31:
            return Date(1, 1, Year(D)+1)
    else:
        return "False"

def Yesterday(D):
    if Day(D) == 1:
        if Month(D) == 12 or Month(D) == 3 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10:
            return Date(30, Month(D)-1, Year(D))
        elif Month(D) == 2:
            if IsKabisat(Year(D)) == True:
                return Date(29, 2, Year(D))
            else:
                return Date(28, 2, Year(D))
        elif Month(D) == 4 or Month(D) == 6 or Month(D) == 9 or Month(D) == 11:
            return Date(31, Month(D), Year(D))
        elif Month(D) == 1:
            return Date(31, 12, Year(D)-1)
    else:
        return Date(Day(D)-1, Month(D), Year(D))            

def NextNday(D, N):
    if N == 1:
        return Nextday(D)
    else:
        return NextNday(Nextday(D), N-1)

def dpm(b): 
    if(b == 1):
      return 1
    elif(b == 2):
        return 32
    elif(b == 3):
        return 60
    elif(b == 4):
        return 91
    elif(b == 5):
        return 121
    elif(b == 6):
        return 152
    elif(b == 7):
        return 182
    elif(b == 8):
        return 213
    elif(b == 9):
        return 244
    elif(b == 10):
        return 274
    elif(b == 11):
        return 305
    elif(b == 12):
        return 335
    else:
        return "Invalid"

def HariKe1900(D):
    return Day(D) + dpm(Month(D)) if Month(D) > 2 and IsKabisat(D) == True else Day(D)-1 + dpm(Month(D))

def IsEqD(D1, D2):
    return HariKe1900(D1) == HariKe1900(D2) and Year(D1) == Year(D2)

def IsBefore(D1, D2):
    if Year(D1) < Year(D2):
        return "True"
    elif Year(D1) == Year(D2):
        return "True" if HariKe1900(D1) < HariKe1900(D2) else "False"
    else:
        return "False"

def IsAfter(D1, D2):
    if Year(D1) > Year(D2):
        return "True"
    elif Year(D1) == Year(D2):
        return "True" if HariKe1900(D1) > HariKe1900(D2) else "False"
    else:
        return "False"

def IsKabisat(D):
    return "True" if (Year(D) % 4 == 0 and Year(D) % 100 != 0) or Year(D) % 400 == 0 else "False"

# Aplikasi :
p = Date(17,10,2002)
q = Date(30,4,2001)

print(Day(p))
print(Month(p))
print(Year(p))
print("{},{},{}".format(Day(Nextday(q)), Month(Nextday(q)), Year(Nextday(q))))
print("{},{},{}".format(Day(Yesterday(q)), Month(Yesterday(q)), Year(Yesterday(q))))
print(HariKe1900(p))
print(IsEqD(p,q))
print(IsBefore(p,q))
print(IsAfter(p,q))
print(IsKabisat(p))
print(IsKabisat(q))
print("{},{},{}".format(Day(NextNday(p,10)), Month(NextNday(p,10)), Year(NextNday(p,10))))