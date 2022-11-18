#contoh 8.1
A = [[5,0],
     [2,6]]
print("A = ",A)

B = [[5,0,8],
     [2,6,7],
     [1,3,4]]
print("B = ",B)

C = [[1,4,5,12],
     [-5,8,9,0],
     [-6,7,11,19]]
print("C = ",C)


#contoh 8.2

#menampilkan nilai pada setiap index/elemen matriks
print("Matriks A = ")
for index_baris in range (len(A)):
    for index_kolom in range (len(A[index_baris])):
        print(A[index_baris][index_kolom])
print("Matriks B = ")
for index_baris in range (len(B)):
    for index_kolom in range (len(B[index_baris])):
        print(B[index_baris][index_kolom], end=' ')
    print()
print("Matriks C = ")
for baris in C:
    print(baris)


#contoh 8.3
#Mengakses nilai pada matriks
print("C[1] = ", C[1])#2nd row
print("C[1][2] = ", C[1][2])#3rd element of 2nd row
print("C[0][-1] = ",C[0][-1])#last element if 1st row

column = [];#empety list
for row in C:
    column.append(row[3])#adds a single item to the existing list
print("3rd column = ",column)

#contoh 8.4
#penjumlahan matriks
mat1 = [[6,0,4],
        [2,7,3],
        [1,6,2]]
mat2 = [[2,6,5],
        [3,2,4],
        [7,1,3]]

result = []
for i in range(len(mat1)):
    row = []
    for j in range (len(mat1[i])):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)
print("Hasil penjumlahan adalah : ")
for row in result:
    print(row)


#contoh 8.5
#perkalian matriks
result = []
for i in range(len(mat1)):
    row = []
    for k in range(len(mat2[0])):
        val = 0
        for j in range(len(mat1[i])):
            val += mat1[i][j] * mat2[i][k]
        row.append(val)
    result.append(row)

print("Hasil perkalian matriks = ")
for row in result:
    print(row)
                           
#tugas praktikum
print()
m = [[2,13,24],
     [20,11,23],
     [34,26,10]]
n = sum(m[0]) + sum(m[1]) + sum(m[2])
print("jumlah =",n)
p = len(m[0])+len(m[1])+len(m[2])
print("len(panjang) = ",p)
rata = n/p
print("Rata - Rata = ",rata)

print()
a = [[1,5,7,9,10],
     [6,20,12,17,38],
     [40,37,22,41,49],
     [50,34,48,29,30],
     [42,32,35,46,48]]
print("A = ",a)
print()

b = max(a[3])
print("Nilai terbesar elemen ke-3 = ",b)
print()

c = min(a[4])
print("Nilai terkecil elemen ke-5 = ",c)

