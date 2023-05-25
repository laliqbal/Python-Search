def sequantial_serch_most_frequent(data):
    count_dict = {}
    for item in data:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item] = 1
    most_frequent = None
    max_coun = 0
    for key in count_dict:
        if count_dict[key]> max_coun:
            most_frequent = key
            max_coun = count_dict[key]
    return most_frequent
my_list = [3,7,2,5,7,3,7,2,7]
frequent_element = sequantial_serch_most_frequent(my_list)
print(f"Elemen yang paling sering muncul adalah {frequent_element}")