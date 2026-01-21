import random

def main():
    print("=== Program Tebak Angka ===")
    
    while True:
        target = random.randint(1, 100)
        percobaan = 0

        while True:
            tebakan = int(input("Tebak angka antara 1-100: "))
            percobaan += 1

            if tebakan > target:
                print("Terlalu besar, coba lagi...")
            elif tebakan < target:
                print("Terlalu kecil, coba lagi...")
            else:
                print(f"Benar! Angka yang dicari adalah {target}")
                print(f"Jumlah percobaan: {percobaan}")
                break

        ulang = input("Ingin bermain lagi? (Y/N): ").strip().upper()
        if ulang != "Y":
            print("Terima kasih, program selesai.")
            break

if __name__ == "__main__":
    main()
