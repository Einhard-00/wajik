#input user
print(43*'=')

print('-hanya bisa untuk bilangan ganjil \n-jika genap maka akan di ganjilkan ke bawah\n-bilangan harus integer')
print(43*'=')
b = int(input('masukkan angka : '))

print(43*'=')

# varieabel pengulangan yang telah terjadi
a = 1

#variabel pengulangan  bintang
c = 1

#variabel spasi dari kiri
d = int(b/2)

#kode pengulangan
while True :
    
    if a %2:       
        print(d*' ','*'*c)
        a += 1
        c += 1
        d -= 1
    else:
        a += 1
        c += 1
        continue

    a += 1   
    c += 1

    if a > b :
        break

b -= 1

while True:

    if a % 2:
        a += 1
        
        c -= 2
        d += 1
        print((1+d)*' ','*'*(c-2))

    else:
        a += 1
        
        continue
    
    if a > (2*b):
        break

print(43*'=')

#karya iqbal 