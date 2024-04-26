# Nama file: Penanggalan_v2.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 18 September 2021
# Deskripsi: Menghitung hari dengan memperhitungkan tahun kabisat

# Definisi dan spesifikasi :
# Harike1900 : integer[1..31], integer[1..12], integer[0..99] --> integer[1..366]
#   {Harike1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung
# mulai 1 Januari 1900+y. 1 Januari tahun 1900+y adalah hari ke 1}
#
# dpm : integer[1..12] --> integer[1..36]
#   {dpm(m) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan m. Terhitung
# mulai 1 Januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1
# bulan m}
#
# IsKabisat : integer[0..99] --> boolean
#   {IsKabisat(a) true jika tahun 1900+a adalah tahun kabisat: habis dibagi 4
# tetapi tidak habis dibagi 100 atau habis dibagi 400}

# Realisasi :
def dpm(m): #analisa kasus terhadap m
    if(m==1):
      return 1
    elif(m==2):
        return 32
    elif(m==3):
        return 60
    elif(m==4):
        return 91
    elif(m==5):
        return 121
    elif(m==6):
        return 152
    elif(m==7):
        return 182
    elif(m==8):
        return 213
    elif(m==9):
        return 244
    elif(m==10):
        return 274
    elif(m==11):
        return 305
    elif(m==12):
        return 335

def IsKabisat(a):
    return (((1900+a) % 4 == 0) and ((1900+a) % 100 != 0) or ((1900+a) % 400 == 0))
    
def Harike1900(d,m,y):
    if m>2 and IsKabisat(y):
        return dpm(m) + d -1 + 1
    else:
        return dpm(m) + d - 1

# Aplikasi :
print(Harike1900(17,10,12))
print(Harike1900(15,4,12))
print(Harike1900(14,2,11))
