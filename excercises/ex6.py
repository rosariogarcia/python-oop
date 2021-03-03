# Print all arguments from functions with its type
# expected esult: retornar un string, cada argumento separado por '-' : "arg1 - arg2 - arg3"
def my_print(*args):
    result=args[0]
    for arg in args:
        result = f"{result} - {arg}"
    return str(result)
 
print(my_print("arg","arg1","arg2","arg3", "arg4"))
print(type(my_print("arg","arg1","arg2","arg3", "arg4")))