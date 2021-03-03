# ------------------------LISTAS----------------------
# Se crean con corchetes vacios

#create:
my_list = [] #lista vacia
my_list = ["python","is","so","cool"] #lista con datos
print(my_list)

#formas de inicializar:
my_list=list()
my_list=list(["is","so","cool","python"])
my_list=list(("python","is","so","cool"))
print(my_list)

my_list=["python",23,[], 45,'c']
print(my_list)

# tamaño de una lista:
size = len(my_list)
print(size)

#Acceder a los elementos:
my_list=["python","is","so","cool"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[1:])
print(my_list[1:3])
print(my_list[1:15])
print(my_list[:3])

# insert() function
my_list=["this","a","list"]
my_list.insert(1,"is")
print(my_list)

# append() function
my_list=["this","is","a"]
my_list.append("list")
print(my_list)

# remove items:
my_list=["this","is","a","list","test"]
my_list.remove("test")
print(my_list)

my_list=["this","is","a","list","test","list"]
my_list.remove("list")
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[1]
print(my_list)

my_list.clear()
print(my_list)

# index() retorna el indice del elemento:
my_list=["this","is","a","list","test"]
index= my_list.index("test")
print(index)

# for and IF statement:
for item in my_list:
    if item == "list":
        continue
    print(item)

# comprehension for:



# Ex 1:
memory_1 = ["M", "na", "i", "Jo", "Bla"]
memory_2 = ["y", "me", "s", "e", "ck"]
result=[]
 ##iterar 2 listas al mismo tiempo?, considerar que las listas debnen ser del mismo tamanño
for m1, m2 in zip(memory_1, memory_2):
    result.append(m1+m2)
print(result)

# Ex-4:
# A crazy trainer returns my grade into single string
# and I need to know the total and the average
# "English=68 Logic=75 Uml=87 Code=80"
string_grade="English=68 Logic=75 Uml=87 Code=80"

# Ex-5:
# I would like to change my first option that was 20 for 2000
# options=[5,10,15,20,25,30,4,20]