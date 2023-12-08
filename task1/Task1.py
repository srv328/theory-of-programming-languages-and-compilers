L1 = input("Введите цепочки языка L1 через пробел: ")
L2 = input("Введите цепочки языка L2 через пробел: ")
if (len(L1.split(' ')) > 10000 or len(L2.split(' ')) > 10000):
    print("Количество цепочек слишком большое!")
    exit()
else:
    for chain in L1:
        if len(chain) > 100:
            print("Цепочка в L1 слишком длинная:", chain)
            exit()
    for chain in L2:
        if len(chain) > 100:
            print("Цепочка в L2 слишком длинная:", chain)
            exit()
listL1 = L1.split(' ')
listL2 = L2.split(' ')


concatenated_language = []  

for chain1 in listL1:
    for chain2 in listL2:
        concatenated_chain = chain1 + chain2 
        concatenated_language.append(concatenated_chain) 
answer = ""
for chain in concatenated_language:
    answer += chain+' '
print(answer)
