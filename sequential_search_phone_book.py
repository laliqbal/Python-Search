def find_phone_number(name, phone_book):
    for contact_name, phone_number in phone_book.items():
        if contact_name == name:
            return phone_number
    return None

# Daftar Buku telepon
phone_book = {
    "David Lejen": "0888-999-555-333",
    "Jane Smith": "0843-555-333-432",
    "Michael Johnson": "087-811-223-344",
    "Emily Davis": "082-122-232-425"
}

# Nama yang ingin dicari nomor teleponnya
name = "Jane Smith"

# Menemukan nomor telepon Jane
phone_number = find_phone_number(name, phone_book)

# Menampilkan nomor telepon Jane
if phone_number:
    print("Nomor telepon", name, "adalah", phone_number)
else:
    print("Nomor telepon", name, "tidak ditemukan.")
