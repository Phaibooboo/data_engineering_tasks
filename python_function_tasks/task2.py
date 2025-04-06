list_1 = ['first name', 'last_name', 'date of birth']

list_2 = [item.replace(" ", "_") for item in list_1]

print(list_2)