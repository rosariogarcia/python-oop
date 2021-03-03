#Ex-5. Replace value
#I would like to change my first option that was 20 for 2000
# options = [5, 10, 15, 20, 25, 30, 4, 20]
options = [5, 10, 15, 20, 25, 30, 4, 20]

#new_options = [option.replace(20, 2000) if option == 20 for option in options ]
count = 0
for option in options:
    if option==20 and count<1:
        index_option = options.index(option)
        del options[index_option]
        options.insert(index_option,2000)
        count+=1
print(options)