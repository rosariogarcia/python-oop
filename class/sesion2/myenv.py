print("Hello wolrd")
name = "Rosario"
lastname = "Garcia"

print ("{} {}".format(name, lastname))
print ("{0} {1}".format(name, lastname))
print (f"{name} {lastname}")

#count: returns the number of words found ina text
large_text = """Thistest is for an example for pthon"""
print (large_text.count("for"))
print (large_text.count("dff"))

# Replace function
txt = "This is a text to replace"
new_txt = txt.replace("to", "for")
print(new_txt)

# Strip() funtion
txt = "            Hello World      "
new_txt = txt.strip()
print(txt)
print(new_txt)

txt = " -----++++***,Hello World -.-.-.-.-.-.-."
new_txt = txt.strip("-*, .+")
print(txt)
print(new_txt)

# *****Ex 2:
post="Adolf not was the only one in his politic, there was other tree adolf's aDolf Junior. adolF, middle and the big ADOLF."
all_lower=post.lower()
all_upper=post.upper()
print(all_lower.count("adolf"))
print(all_upper.count("ADOLF"))

# title() funtion
fullname = "rosario garcia"
print(fullname.title())

# split() funtion
names_lista = fullname.split()
print(names_lista)
names_lista_wrong = fullname.split("-")
print(names_lista_wrong)
fullname_1 = "rosario-garcia"
names_lista1 = fullname_1.split("-")
print(names_lista1)

# find() function: retorna el indice de la palabra que se busca
txt = "esto es uun texto para tests find function"
index= txt.find("texto")
print(index)

# cast
str_num = "23"
num = int(str_num)
print(str_num, type(str_num))
print(num, type(num))

# len() retorna el tamaño de la cadena
print(len(str_num))

