print(10*"=","MY CALCULATE BMI","="*10)
"""
menginput nama,berat badan,tinggi badan

"""
nama = input("Masukkan nama = ")
berat_badan = float(input("Masukkan berat badan = "))
tinggi_badan = float(input("Masukkan tinggi badan = "))
keterangan = ("BMI anda adalah ")
#menghitung bmi
bmi = berat_badan/(tinggi_badan * tinggi_badan)
print("BMI = ",bmi)
#proses membandingkan BMI
if (bmi < 17.0):
	print(keterangan,"Kurus,kekurangan berat badan")
elif(bmi >= 17.0 and bmi <= 18.4):
	print(keterangan,"Kurus,kekurangan berat badan dan ringan")
elif(bmi >= 18.5 and bmi <= 25.0):
	print(keterangan,"Normal")
elif(bmi >= 25.0 and bmi <= 27.0):
	print(keterangan,"Gemuk,kelebihan berat badan tingkat ringan")
else:
	print(keterangan,"Gemuk,kelebihan berat badan tingkat berat")
	