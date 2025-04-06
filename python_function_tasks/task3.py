name_list = ['Mayowa', 'chizoba', 'Chigozie']
name_list2 = []

for name in name_list:
    
    if name[0].isupper() == True and name[-1] == 'a':
        name_list2.append(name)
    elif name[0].isupper() == True and name[-1] != 'a':
        new_name = name[:-1] + 'a'
        name_list2.append(new_name)
        
print(name_list2)
        
