def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celcius_ke_kelvin(c):
    return c + 273.15

def menu():
    print("\n=== APLIKASI KONVERTER SUHU ===")
    print("1. Celcius ke Fahrenheit")
    print("2. Celcius ke Kelvin")
    print("3. Keluar")

if __name__ == "__main__":
    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3): ")
        if pilihan == '1':
            suhu = float(input("Masukkan suhu dalam Celcius: "))
            print(f"Hasil: {suhu}C = {celcius_ke_fahrenheit(suhu)}F")
        elif pilihan == '2':
            suhu = float(input("Masukkan suhu dalam Celcius: "))
            print(f"Hasil: {suhu}C = {celcius_ke_kelvin(suhu)}K")
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")