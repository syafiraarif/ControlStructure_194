#tugas 1
#membuat fungsi nilai mahasiswa bertipe data int 
nilaimahasiswa = int( input('nilai mahasiswa ='))

#membuat beberapa kondisi dengan syarat yang sudah di tentukan
if nilaimahasiswa >= 90:              #jika nilai mahasiswa >= 90 maka akan menampilkan "Excellent performance"
    print('Excellent performance')
elif nilaimahasiswa >= 80:            #jika nilai mahasiswa >= 80 maka akan menampilkan "Very Good performance"
    print('Very Good performance')
elif nilaimahasiswa >= 70:            #jika nilai mahasiswa >= 70 maka akan menampilkan "Good performance"
    print('Good performance')
elif nilaimahasiswa >= 60:            #jika nilai mahasiswa >= 60 maka akan menampilkan "Average performance"
    print('Average performance')



#tugas 2
#membuat fungsi angka terbesar untuk mencari angka terbesar dari 3 nilai yang di berikan
def angkaTerbesar (a,b,c):
    if  a >= b and a >= c:          #membandingkan antara nilai a,b dan c, jika a lebih besar dari b dan c maka tampilkan nilai a
        return a
    elif b >= a and b >=c:          #membandingkan antara nilai a,b dan c, jika b lebih besar dari a dan c maka tampilkan nilai a
        return b
    else :                          #jika tidak kedua kondisi di atas maka nilai yang paling besar adalah c
        return c

#masukan nilai yang di inginkan
angka1 = int( input('angka pertama ='))
angka2 = int( input('angka kedua ='))
angka3 = int( input('angka ketiga ='))

#menampilkan angka yang paling besar dengan memanggil fungsi angkaTerbesar
print('angka terbesar adalah', angkaTerbesar(angka1,angka2,angka3))

#tugas 3
#memasukan nilai N
n = int(input("nilai N = "))
a, b = 0, 1

#Menggunakan perulangan while untuk mencetak angka Fibonacci sampai a kurang dari atau sama dengan n
while a <= n:
    print(a, end=" ")          
    a, b = b, a + b
    

#tugas 4
#memasukan nilai N untuk Mencetak Bilangan Ganjil Hingga n
n = int(input("Masukkan batas atas: "))  # Input batas atas hingga n

for i in range(1, n + 1):  # Loop dari 1 hingga n
    if i % 2 != 0:  # Jika i adalah bilangan ganjil
        print(i, end=" ")  # Cetak bilangan ganjil

#tugas 5
#membuat fungsi untuk mencetak segitiga angka
def segitiga_angka():

#memasukan nilai N
    n = int(input("Masukkan nilai n untuk segitiga angka: "))
 #Menggunakan loop for untuk mencetak setiap baris segitiga
    for i in range(1, n + 1):
# Mencetak angka i sebanyak i kali, diikuti dengan spasi
        print((str(i) + ' ') * i)

# Memanggil fungsi untuk menjalankan program
segitiga_angka()