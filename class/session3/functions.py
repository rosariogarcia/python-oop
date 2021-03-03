# -----functions-----
# identation de 4 puntos, 4 espacios
# puede no tener parametros
def greet():
    #pass:
    pass

# puede tener uno o mas parametros
def greet_parameters(name1, name2):
    print(f"Hello {name1} and {name2}")

# cantidad de parametros no definidos
def greet_qty_parameters_undefined(*names):
    print(f"Hello {names}")
    print(f"Hello {names[0]},{names[1]}")

# Las funciones se llaman con parentesis y enviar los parametros si requiere
greet_parameters("Cha", "Sofi")
greet_qty_parameters_undefined("Jose","Gabi","Nancy")

# Keyword arguments: llamar a la funcion especificando el nombre de parametro:
def greet_keyword(name, lastname):
    print("Hello", name, lastname)

greet_keyword(lastname="Garcia", name="Sofi")

# **kwargs: envia los paametros como dictionary(key, value)
def greet_kwargs(**kwargs):
    print(type(kwargs))
    print("Hello", kwargs["name"], kwargs["lastname"])

greet_kwargs(lastname="Garcia",name="Sofi")


#print with end:
print("Hello", "name", "lastname", end=",")

#function with parameter with default value:
def gree_with_defaul_value(name="Sofi"):
    print(f"Heloo {name}")

gree_with_defaul_value()
gree_with_defaul_value("My friend")

# python permite enviar diferentes tipos de datos
# si la funcion no retorna naa, python por defecto retorna NoNE:
gree_with_defaul_value("ghc")
gree_with_defaul_value(123)
gree_with_defaul_value(object)


#funtions with return
def get_name():
    return "Joshua"

print(f"Hello {get_name()}")









