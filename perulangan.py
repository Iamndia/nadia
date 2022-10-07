"""
perulangan

"""
print(4*"=","Menampilkan angka genap 1 - 100 yang bisa dibagi 5","="*4)
for i in range(1,100+1):
	if (i%2 == 0 and i%5 == 0):
		print(i)