# Las tuplas no se pueden modificar los valores
# no se puede remover algunos elementos
# en ocasiones en mejor usar tuplas para evitar que se corrompas los valores


# create tuple
my_tuple = ("this","is","a","tuple")
print(my_tuple)

#create:
my_tuple = [] #tuple vacia
my_tuple = ["python","is","so","cool"] #tuple con datos
print(my_tuple)

#formas de inicializar:
my_tuple=tuple()
my_tuple=tuple(["is","so","cool","python"])
my_tuple=tuple(("python","is","so","cool"))
print(my_tuple)

my_tuple=["python",23,[], 45,'c']
print(my_tuple)

# tamaño de una tuple:
size = len(my_tuple)
print(size)

#Acceder a los elementos:
my_tuple=["python","is","so","cool"]
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[-2])
print(my_tuple[-3])
print(my_tuple[1:])
print(my_tuple[1:3])
print(my_tuple[1:15])
print(my_tuple[:3])

# insert() function
my_tuple=["this","a","tuple"]
my_tuple.insert(1,"is")
print(my_tuple)

# append() function
my_tuple=["this","is","a"]
my_tuple.append("tuple")
print(my_tuple)

# remove items:
my_tuple=["this","is","a","tuple","test"]
my_tuple.remove("test")
print(my_tuple)

my_tuple=["this","is","a","tuple","test","tuple"]
my_tuple.remove("tuple")
print(my_tuple)

my_tuple.pop(1)
print(my_tuple)

del my_tuple[1]
print(my_tuple)

my_tuple.clear()
print(my_tuple)

# index() retorna el indice del elemento:
my_tuple=["this","is","a","tuple","test"]
index= my_tuple.index("test")
print(index)

# for and IF statement:
for item in my_tuple:
    if item == "tuple":
        continue
    print(item)

# comprehension for:



# Ex 1:
memory_1 = ["M", "na", "i", "Jo", "Bla"]
memory_2 = ["y", "me", "s", "e", "ck"]
result=[]
 ##iterar 2 tuples al mismo tiempo?, considerar que las tuples debnen ser del mismo tamanño
for m1, m2 in zip(memory_1, memory_2):
    result.append(m1+m2)
print(result)