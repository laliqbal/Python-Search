def sequental_search(data, key):
    for item in data:
        if item == key:
            return True
    return False
my_list = [3,4,5,6,7]
key = 6
found = sequental_search(my_list,key)
if found:
    print("Elemen DiTentukan.")
else:
    print("Elemen Tidak DiTentukan")