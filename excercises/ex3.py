#Ex-3. Concatenate lists (who I am)
#I had a transit accident and I don't remember my name help me please!!

memory_1 = ["M", "na", "i", "Jo", "Bla"]
memory_2 = ["y", "me", "s", "e", "ck"]
result=[]
##iterar 2 listas al mismo tiempo?, considerar que las listas debnen ser del mismo tamanño
for m1, m2 in zip(memory_1, memory_2):
    result.append(m1+m2)
print(result)