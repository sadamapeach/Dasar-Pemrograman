# Nama file: JARAK2TITIK, Least Square.py
# Pembuat: Oktaviana Sadama Nur Azizah
# Tanggal: 4 September 2021
# Deskripsi: sebuah fungsi yang menerima empat buah bilangan riil, dimana dua
# pasang titik pada koordinat kartesian, dan menghasilkan sebuah bilangan riil
# yang merupakan jarak dari kedua titik tersebut, dengan melakukan aplikasi
# terhadap dua buah fungsi antara yang harus didefinisikan terlebih dulu

# Deskripsi dan spesifikasi dari fungsi JARAK2TITIK, Least Square bernama LS
# (x1,x2,y1,y2) adalah:
# LS : 4 real --> real
#   {LS (x1,x2,y1,y2) adalah jarak antara dua buah titik (x1,x2} dengan (y1,y2)}
# dif2 : 2 real --> real
#   {dif(x,y) adalah kuadrat dari selisih antara x dan y}
# FX2 : real --> real
#   {FX2(x) adalah hasil kuadrat dari x}

# Realisasi
def FX2(x):
    return (x*x)
def dif2 (x,y):
    return FX2(x - y)
def LS (x1,y1,x2,y2):
    return ((dif2(y1,y2)) + (dif2(x2,x1)))**0.5

# Aplikasi
print (LS(1,3,5,6))
