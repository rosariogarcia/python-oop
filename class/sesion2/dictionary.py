# sintaxis similar json
# create dictionary
# {<Key>:<Value>}
my_dict={}
my_dict = {"type":"Car", "Brand":"Ford","Model":"Mustang","Year":2020,
34:45, object:"test"}
print(my_dict)


# ----Accessing Items----

# Using the name of Key
model=my_dict["Model"]
print(model) 

# Using get() function
model=my_dict.get("Model")
print(model)
model=my_dict.get("Price","There is no Price in dict")
print(model)  

# Getting all Keys
keys = my_dict.keys()
for key in keys:
    print (f"Key: {key}")

# getting all values
values = my_dict.values()
for value in values:
    print (f"Value: {value}")

# getting key and value at the same time
items = my_dict.items()
for key, value in items:
    print (f"{key}:{value}")

# ------SETTING DICT------
my_dict = {"type":"Car", "Brand":"Ford","Model":"Mustang","Year":2020,
34:45, object:"test"}
#Using the key name
# Si is elemento no existe lo agrega an final del diccionario
my_dict["Year"]=2021
print(my_dict)
my_dict["Owner"] = "Cha"
print(my_dict)

#Using update() function
# Si is elemento no existe lo agrega an final del diccionario
my_dict.update({"Brand":"Toyota"})
print(my_dict)


# ------Removin elements from DICT------
# pop() funtion
my_dict = {"type":"Car", "Brand":"Ford","Model":"Mustang","Year":2020,
34:45, object:"test"}
##Returns the value deleted
print(my_dict.pop("type"))

# del() funtion
my_dict = {"type":"Car", "Brand":"Ford","Model":"Mustang","Year":2020,
34:45, object:"test"}
del my_dict["Brand"]
print(my_dict)

# WARNING: you are deleting all dictionary
#del my_dict
#print(my_dict)

#Se puede crear diccionarios anidados
#No se puede tener un dictionario como key.
dic_anidaddo={"Dict1":{"Dict2":{"Dic3":3}}}
print(dic_anidaddo)