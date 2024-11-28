file = open("data_rafli.txt", "w")
file.write(f"nama : {input('Masukkan nama : ')}\n")
file.write(f"umur : {input('Masukkan umur : ')}\n")
file.write(f"alamat : {input('Masukkan alamat : ')}\n")
file.write(f"email : {input('Masukkan email : ')}\n")
file.write(f"dosen : {input('Masukkan nama dosen : ')}\n")

file.close()

file = open("data_rafli.txt", "r")
data = file.read() 
print("\nData yang tersimpan di file:")
print(data)
file.close()
