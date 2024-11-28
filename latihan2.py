import traceback

def buat_file(file_name):
    """Membuat file baru dengan nama yang diberikan dan menulis data awal.

    Args:
      file_name: Nama file yang akan dibuat.
    """
    try:
        with open(file_name, 'w') as file:
          
            user_name = input("nama anda: ")
            user_nim = input("nim anda: ")
            year_of_entry = input("tahun angkatan: ")

            file.write(f"nama anda: {user_name}\n")
            file.write(f"nim anda: {user_nim}\n")
            file.write(f"tahun angkatan: {year_of_entry}\n")
            
            print("File berhasil dibuat")
    except Exception as e:
        print("Terjadi kesalahan saat membuat file:")
        traceback.print_exc()  

def baca_file(file_name):
    """Membaca isi file dan menampilkannya ke layar.

    Args:
      file_name: Nama file yang akan dibaca.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("File kosong")
    except FileNotFoundError:
        print("File tidak ditemukan")
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:")
        traceback.print_exc()  

def tambah_teks(file_name):
    """Menambahkan teks ke dalam file yang sudah ada.

    Args:
      file_name: Nama file yang akan ditambahkan teks.
    """
    try:
        with open(file_name, 'a') as file:
          
            teman = input("masukan nama sahabatmu: ")
            catatan = input(" Masukan note tambahan: ")
            
            file.write(f"masukan nama sahabatmu: {teman}\n")
            file.write(f"Masukan note tambahan: {catatan}\n")
            print("Teks berhasil ditambahkan")
    except FileNotFoundError:
        print("File tidak ditemukan")
    except Exception as e:
        print("Terjadi kesalahan saat menambah teks ke file:")
        traceback.print_exc()  

def menu():
    """Menampilkan menu pilihan dan memanggil fungsi yang sesuai."""
    while True:
        print("\n--- File Handling ---")
        print("1. Buat File Baru")
        print("2. Baca File")
        print("3. Edit File")
        print("9. Keluar")
        pilihan = input("Pilihan (1/2/3/9): ")

        if pilihan == '1':
            file_name = input("Nama File: ")
            buat_file(file_name)
        elif pilihan == '2':
            file_name = input("Nama File: ")
            baca_file(file_name)
        elif pilihan == '3':
            file_name = input("Nama File: ")
            tambah_teks(file_name)
        elif pilihan == '9':
            print("Bye Bye :3")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    menu()
