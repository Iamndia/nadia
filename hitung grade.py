input_nilai = int(input("Masukkan nilai = "))
nilai = input_nilai
print("Nilai = ",nilai)

if input_nilai >= 90:
	print("Grade A")
elif input_nilai >= 80 and  input_nilai < 90:
	print("Grade B")
elif input_nilai >= 60 and  input_nilai < 80:
	print("Grade C")
elif input_nilai >= 40 and  input_nilai < 60:
	print("Grade D")
else:
	print("Grade E")
if nilai >= 70:
	print("Lulus")
elif nilai < 70:
	print("tidak lulus")
